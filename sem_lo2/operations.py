"""Operations: selling and purchasing products"""

from .storage import load_json, save_json
from .models.product import ProductCatalog, Product
from .models.finance import Finance, Transaction
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
PRODUCTS_PATH = os.path.join(DATA_DIR, "products.json")
FINANCES_PATH = os.path.join(DATA_DIR, "finances.json")


def load_products():
    data = load_json(PRODUCTS_PATH) or {"products": []}
    return ProductCatalog.from_list(data.get("products", []))


def save_products(catalog: ProductCatalog):
    save_json(PRODUCTS_PATH, {"products": catalog.to_list()})


def load_finances():
    data = load_json(FINANCES_PATH) or {"balance": 0.0, "transactions": []}
    return Finance.from_dict(data)


def save_finances(fin: Finance):
    save_json(FINANCES_PATH, fin.to_dict())


def sell_product(user, product_id: str, quantity: int):
    # only admin or role 'seller' allowed
    if user.role not in ("admin", "seller"):
        raise PermissionError("User does not have permission to sell")
    catalog = load_products()
    p = catalog.find(product_id)
    if not p:
        raise ValueError("Product not found")
    if p.stock < quantity:
        raise ValueError("Not enough stock")
    p.stock -= quantity
    save_products(catalog)

    fin = load_finances()
    total = p.price * quantity
    tx = Transaction.create(kind="sale", amount=total, by_user=user.username, details=f"Sold {quantity} x {p.name}")
    fin.apply(tx)
    save_finances(fin)
    return tx


def purchase_product(user, product_id: str, quantity: int, unit_price: float = None):
    # purchase increases stock and decreases balance (cost)
    if user.role not in ("admin", "purchaser"):
        raise PermissionError("User does not have permission to purchase")
    catalog = load_products()
    p = catalog.find(product_id)
    if not p:
        raise ValueError("Product not found")
    p.stock += quantity
    if unit_price is not None:
        p.price = unit_price
    save_products(catalog)

    fin = load_finances()
    cost = -abs((unit_price or p.price) * quantity)
    tx = Transaction.create(kind="purchase", amount=cost, by_user=user.username, details=f"Purchased {quantity} x {p.name}")
    fin.apply(tx)
    save_finances(fin)
    return tx
