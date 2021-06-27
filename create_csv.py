import pandas as pd
from dataclasses import dataclass
from Product import Product

df = pd.read_csv("/home/karlis/Desktop/products_oakley_import.csv")
output_csv_fn = "oakley_glasses.csv"

# vincere 

row = df.iloc[0]


products = [
    Product("Latch Beta Prizm Tungsten - Olive Ink", "Oakley", 1, "Sunglasses", 300, price_low=78, price=155.95, sku="OO9436-0354"),
    Product("Frogskins Prizm Grey - Polished Black", "Oakley", 1, "Sunglasses", 300, price_low=52.5, price=104.95, sku="24-306"),
    Product("Holbrook Red Iridium - Matte Black", "Oakley", 1, "Sunglasses", 300, price_low=67.5, price=134.95, sku="OO9102-36"),
    Product("Holbrook Prizm Ruby - Matte Black", "Oakley", 1, "Sunglasses", 300, price_low=72.5, price=144.95, sku="OO9102-E255"),
    Product("Latch Prizm Gray - Matte Black", "Oakley", 1, "Sunglasses", 300, price_low=73, price=145.95, sku="OO9265-5653"),
    Product("Frogskins Lite Prizm Black - Ignite Pink", "Oakley", 1, "Sunglasses", 300, price_low=66, price=109.95, sku="OO9374-3263"),
    Product("Manorburn Prizm Violet - Matte Black", "Oakley", 1, "Sunglasses", 300, price_low=62.5, price=102.95, sku="OO9479-0356"),
    Product("Sylas Prizm Black - Matte Black", "Oakley", 1, "Sunglasses", 300, price_low=62.5, price=124.95, sku="OO9448-0357")
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
    row["Cost per item"] = round(product.price_low * 0.8, 2)
    row["Variant SKU"] = product.sku

    print(row)

    new_df = new_df.append(row)
    # new_df.loc[i] = row

print(new_df.head(10))

new_df.to_csv(output_csv_fn, index=False)