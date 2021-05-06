import pandas as pd
import os
import re
import requests
import xml.etree.ElementTree as ET

from Product import Product

XML_URL = "http://intrad.lv/xml/?get&key=MyBeachStore&pass=rinald2021"

example = pd.read_csv("/home/karlis/Desktop/products_oakley_import.csv")
output_csv_fn = "intrad_products.csv"

def get_handle(name):
    handle = name
    handle = re.sub(r'\W+', ' ', handle)
    handle = handle.replace(" ", "-")
    handle = ' '.join(handle.split())
    handle = handle.lower()
    return handle

if __name__ == "__main__":
    response = requests.get(XML_URL)
    xml = ET.fromstring(response.content)

    df = pd.read_csv("intrad_filtered.csv")

    products = []

    new_df = pd.DataFrame(columns=example.columns)

    for i, row in df.iterrows():
        sku = row["SKU"]
        for item in xml:
            art = item.find("art")
            
            if art.text != sku:
                continue

            qty = item.find("qty")
            price = item.find("cena_ar_pvn")
            rrp = item.find("rrp").text
            vendor = item.find("brand_name")
            title = item.find("name_eng")
            imagelink = item.find("imagelink")
            extra_images = item.find("papildus_bildes")

            row = example.iloc[0]
            row["Handle"] = get_handle(title.text)
            row["Vendor"] = vendor.text
            row["Title"] = title.text
            row["Type"] = ""
            row["Variant Inventory Policy"] = "deny"
            row["Variant Inventory Qty"] = int(qty.text)
            if rrp is None:
                row["Variant Price"] = round(float(price.text) / 1.21, 2) * 2.0
                row["Cost per item"] = round(float(price.text) / 1.21, 2)          
            else:
                row["Variant Price"] = round(float(rrp) * 0.75 / 1.21, 2) * 2.0
                row["Cost per item"] = round(float(rrp) * 0.75 / 1.21, 2)
                
            row["Image Src"] = imagelink.text
            row["Image Position"] = 1
            row["Variant SKU"] = sku

            new_df = new_df.append(row)

            if extra_images.text is not None:
                extra_row = {}
                extra_row["Handle"] = get_handle(title.text)
                extra_row["Image Src"] = extra_images.text
                new_df = new_df.append(extra_row, ignore_index=True)


            # product = Product(title.text, qty.text, vendor.text, "Gym",

            #print(title.text, sku, imagelink.text)
            break
    print(new_df.head(10))

    new_df.to_csv(output_csv_fn, index=False)