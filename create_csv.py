import pandas as pd
from dataclasses import dataclass
from Product import Product

df = pd.read_csv("products_oakley_import.csv")
output_csv_fn = "oakley_glasses.csv"

# vincere 

row = df.iloc[0]


products = [
    Product("Sutro S Prizm Road - Matte White", "Oakley", 1, "Sunglasses", 300, price_low=78, price=155.95, sku="OO9462-0528"),
    Product("Sutro S Prizm Trail Torch - Matte Black", "Oakley", 1, "Sunglasses", 300, price_low=78, price=155.95, sku="OO9462-0328"),

    Product("Sutro Lite Prizm Trail Torch - Matte Carbon", "Oakley", 1, "Sunglasses", 300, price_low=83, price=165.95, sku="OO9463-0439"),
    Product("Sutro Lite Prizm Road - Matte White", "Oakley", 1, "Sunglasses", 300, price_low=83, price=165.95, sku="OO9463-0239"),
    Product("Sutro Lite Prizm Black - Patrick Mahomes II Collection", "Oakley", 1, "Sunglasses", 300, price_low=93, price=185.95),

    Product("Radar® EV Path® Prizm Grey - Matte Cool Grey", "Oakley", 1, "Sunglasses", 300, price_low=88.5, price=176.95, sku="OO9208-B938"),
    Product("Radar® EV Path® Prizm Grey - Odyssey Collection Holographic", "Oakley", 1, "Sunglasses", 300, price_low=93, price=186.95, sku="OO9208-C538"),
    Product("Radar® EV Path® Prizm Black - Electric Purple Shadow Camo", "Oakley", 1, "Sunglasses", 300, price_low=104.5, price=208.95, sku="OO9208-A238"),
    Product("Radar® EV Path® Prizm Black Polarized - Polished White", "Oakley", 1, "Sunglasses", 300, price_low=118.5, price=236.95, sku="OO9208-9438"),

    Product("Radar® EV Path® Prizm Road - Jolt Collection", "Oakley", 1, "Sunglasses", 300, price_low=93, price=186.95, sku="OO9208-A038"),
    Product("Radar® EV Path® Prizm Road Jade - Steel", "Oakley", 1, "Sunglasses", 300, price_low=93, price=186.95, sku="OO9208-A138"),

    Product("Radar® EV Path® Prizm Golf - Polished White", "Oakley", 1, "Sunglasses", 300, price_low=93, price=186.95, sku="OO9208-A538"),
    Product("Radar® EV Path® Prizm Trail Torch - Matte Black", "Oakley", 1, "Sunglasses", 300, price_low=93, price=186.95, sku="OO9208-9038"),
    
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
    row["Variant Grams"] = product.grams
    row["Cost per item"] = product.price_low
    row["Variant SKU"] = product.sku
    row["Tags"] = "_Oak"

    new_df = new_df.append(row)

print(new_df.head(10))

new_df.to_csv(output_csv_fn, index=False)