"""Product models and catalog"""

import uuid
from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    id: str
    name: str
    price: float
    stock: int

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price, "stock": self.stock}

    @staticmethod
    def from_dict(d):
        return Product(id=d.get("id") or str(uuid.uuid4()), name=d["name"], price=float(d["price"]), stock=int(d.get("stock", 0)))


class ProductCatalog:
    def __init__(self, products: List[Product] = None):
        self.products = products or []

    def find(self, product_id):
        for p in self.products:
            if p.id == product_id:
                return p
        return None

    def to_list(self):
        return [p.to_dict() for p in self.products]

    @staticmethod
    def from_list(lst):
        return ProductCatalog([Product.from_dict(d) for d in lst])
