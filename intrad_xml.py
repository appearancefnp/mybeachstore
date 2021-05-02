import os
import cv2
import numpy as np
import glob
import requests
from skimage import io
import csv
import xml.etree.ElementTree as ET

XML_URL = "http://intrad.lv/xml/?get&key=MyBeachStore&pass=rinald2021"

img_dir = "images"

def get_image_from_url(url):
    try:
        response = requests.get(url)
    except Exception as e:
        return None
    # print(response.content)
    data = np.frombuffer(response.content, dtype=np.uint8)
    image = cv2.imdecode(data, cv2.IMREAD_COLOR)
    # print(response.content)
    # return the image
    return image

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

if __name__ == "__main__":
    # get response from intrad server
    response = requests.get(XML_URL)
    # print(xml.content)
    xml = ET.fromstring(response.content)

    IMAGE_WIDTH = 800

    with open("intrad.csv", mode="w") as intrad_csv:
        writer = csv.writer(intrad_csv, delimiter=",")

        header_row = ["Brand", "Title", "Quantity", "Price", "SKU"]
        writer.writerow(header_row)

        # iterate over all items on intrad.lv
        for item in xml:
            qty = item.find("qty")
            price = item.find("cena_ar_pvn")
            vendor = item.find("brand_name")
            title = item.find("name_eng")
            imagelink = item.find("imagelink")
            sku = item.find("art")

            if not (qty is not None and price is not None and vendor is not None and title is not None and imagelink is not None):
                continue


            if (qty.text == None):
                continue

            try:
                qty = int(qty.text)
            except Exception:
                # illegal simbols e.g. >30days
                continue

            csv_row = [vendor.text, title.text, qty, price.text, sku.text]
            writer.writerow(csv_row)
            
            # if (qty == 0):
            #     continue

            # img = get_image_from_url(imagelink.text)
            # if img is None:
            #     print("Image is none")
            #     continue
            # print(title.text)
            # # img = cv2.imread("pic1.jpg")

            # img = image_resize(img, width=IMAGE_WIDTH)

            # # insert product image on the big image
            # final_image = np.full((img.shape[0] + 200, IMAGE_WIDTH, 3), 255, dtype=np.uint8)
            # final_image[0:img.shape[0], 0:] = img

            # # put text
            # color = (0, 0, 0)
            # font = cv2.FONT_HERSHEY_PLAIN
            # thickness = 1
            # # text
            # text_qty = f"QTY: {qty}"
            # text_price = f"Price: {float(price.text) / 1.21}"
            # text_vendor = f"Vendor: {vendor.text}"

            # origin = (5, img.shape[0] + 30)
            # final_image = cv2.putText(final_image, text_qty, origin, font, 1, color, thickness=thickness)
            # origin = (5, origin[1] + 30)
            # final_image = cv2.putText(final_image, text_price, origin, font, 1, color, thickness=thickness)
            # origin = (5, origin[1] + 30)
            # final_image = cv2.putText(final_image, text_vendor, origin, font, 1, color, thickness=thickness)


            # cv2.imwrite(f"images/{title.text}.jpg", final_image)
            # cv2.imshow(f"{title.text}.jpg", final_image)
            # cv2.waitKey(100)
            # print(f"Product: {title.text}, Qty: {qty}")

            # print(item.tag, item.attrib)