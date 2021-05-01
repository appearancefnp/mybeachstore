import pandas as pd
import os
from dataclasses import dataclass
import re

df = pd.read_csv("/home/karlis/Desktop/products_oakley_import.csv")
output_csv_fn = "mikasa.csv"

row = df.iloc[0]

@dataclass
class Product:
    name: str
    quantity: int
    vendor: str
    tips: str
    grams: int
    price: float
    price_low: float

    def __init__(self, name, vendor, quantity, tips, grams, price_low, price = None):
        self.name = name
        self.vendor = vendor
        self.quantity = quantity
        self.tips = tips
        self.grams = grams
        self.price_low = price_low
        self.price = price

    def get_handle(self):
        handle = self.name
        handle = re.sub(r'\W+', ' ', handle)
        handle = handle.replace(" ", "-")
        handle = ' '.join(handle.split())
        handle = handle.lower()
        return handle

    def get_price(self):
        if self.price is None:
            return self.price_low * 2.0
        else:
            return self.price

products = [
    Product("Mikasa VXT 30", "Mikasa", 1, "Balls", 100, price_low=23.5, price=45),
    Product("Mikasa VX 3.5", "Mikasa", 1, "Balls", 100, price_low=6.5, price=15),

    Product("Mikasa Key Ring", "Mikasa", 1, "Accessories", 100, price_low=4.5, price=9),

    Product("Mikasa Whistle WH-2 BK", "Mikasa", 1, "Whistle", 100, price_low=3, price=8),
    Product("Mikasa Whistle RA0070-B", "Mikasa", 1, "Whistle", 100, price_low=4.95, price=12),
    
    Product("Mikasa Ball Bag For 6 Balls AC-BG260W-Blue", "Mikasa", 1, "Bags & Backpacks", 200, price_low=19.05, price=45),
    Product("Mikasa Ball Bag For 6 Balls EK0046-B", "Mikasa", 1, "Bags & Backpacks", 200, price_low=15, price=30),

    Product("Mikasa Hand Pump DHP21-BL", "Mikasa", 1, "Hand Pump", 100, price_low=4.5, price=9),
]


new_df = pd.DataFrame(columns=df.columns)
for i, product in enumerate(products):
    row = df.iloc[0]
    row["Handle"] = product.get_handle()
    row["Vendor"] = product.vendor
    row["Title"] = product.name
    row["Type"] = product.tips
    row["Variant Inventory Qty"] = product.quantity
    row["Variant Price"] = product.get_price()
    row["Cost per item"] = product.price_low

    print(row)

    new_df = new_df.append(row)
    # new_df.loc[i] = row

print(new_df.head(10))

new_df.to_csv(output_csv_fn, index=False)