"""Report generation: plain-text report summarizing company state"""

from .storage import load_json
import os
from .models.product import ProductCatalog
from .models.finance import Finance
from .models.user import User

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
PRODUCTS_PATH = os.path.join(DATA_DIR, "products.json")
USERS_PATH = os.path.join(DATA_DIR, "users.json")
FINANCES_PATH = os.path.join(DATA_DIR, "finances.json")


def generate_report(path="company_report.txt"):
    products_data = load_json(PRODUCTS_PATH) or {"products": []}
    users_data = load_json(USERS_PATH) or {"users": []}
    finances_data = load_json(FINANCES_PATH) or {"balance": 0.0, "transactions": []}

    lines = []
    lines.append("COMPANY REPORT\n")
    lines.append("Users:\n")
    for u in users_data.get("users", []):
        lines.append(f"- {u.get('username')} (role: {u.get('role')})")
    lines.append("\nProducts:\n")
    for p in products_data.get("products", []):
        lines.append(f"- {p.get('name')}: price={p.get('price')}, stock={p.get('stock')}")
    lines.append("\nFinances:\n")
    lines.append(f"Balance: {finances_data.get('balance')}")
    lines.append("Transactions:")
    for t in finances_data.get("transactions", []):
        lines.append(f"- {t.get('kind')} {t.get('amount')} by {t.get('by_user')} details: {t.get('details')}")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return path
