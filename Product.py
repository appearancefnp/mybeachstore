from dataclasses import dataclass
import re

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
