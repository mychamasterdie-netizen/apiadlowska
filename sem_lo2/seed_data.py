"""Seed data generator: creates initial users, products, finances"""

from .storage import save_json
from .auth import _hash_password
import os
import uuid

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
USERS_PATH = os.path.join(DATA_DIR, "users.json")
PRODUCTS_PATH = os.path.join(DATA_DIR, "products.json")
FINANCES_PATH = os.path.join(DATA_DIR, "finances.json")


def generate():
    users = {
        "users": [
            {"id": str(uuid.uuid4()), "username": "admin", "password_hash": _hash_password("adminpass"), "role": "admin", "extra": {}},
            {"id": str(uuid.uuid4()), "username": "seller", "password_hash": _hash_password("sellerpass"), "role": "seller", "extra": {}},
            {"id": str(uuid.uuid4()), "username": "purchaser", "password_hash": _hash_password("purchaserpass"), "role": "purchaser", "extra": {}},
        ]
    }

    products = {
        "products": [
            {"id": str(uuid.uuid4()), "name": "Notebook", "price": 3.5, "stock": 100},
            {"id": str(uuid.uuid4()), "name": "Pen", "price": 1.2, "stock": 200},
            {"id": str(uuid.uuid4()), "name": "Backpack", "price": 25.0, "stock": 20},
        ]
    }

    finances = {"balance": 1000.0, "transactions": []}

    save_json(USERS_PATH, users)
    save_json(PRODUCTS_PATH, products)
    save_json(FINANCES_PATH, finances)
    print("Seed data created in:", DATA_DIR)


if __name__ == "__main__":
    generate()
