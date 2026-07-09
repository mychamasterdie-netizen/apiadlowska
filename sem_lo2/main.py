"""Simple command-line interface (CLI) for the app"""

from .auth import authenticate, find_user, create_user
from .operations import load_products, sell_product, purchase_product
from .report import generate_report
from .storage import load_json
from .models.product import Product
import os


def print_menu(role):
    print("\nAvailable commands:")
    print("  products     - list products")
    if role in ("admin", "seller"):
        print("  sell         - sell a product (seller or admin)")
    if role in ("admin", "purchaser"):
        print("  purchase     - purchase/add stock (purchaser or admin)")
    if role == "admin":
        print("  adduser      - create new user")
        print("  edituser     - edit user role/password")
    print("  report       - generate company report (text file)")
    print("  quit         - exit program")


def repl(user):
    print(f"Logged in as {user.username} (role={user.role})")
    while True:
        print_menu(user.role)
        cmd = input("cmd> ").strip().lower()
        if cmd == "quit":
            break
        elif cmd == "products":
            catalog = load_products()
            for p in catalog.products:
                print(f"{p.id} - {p.name}: price={p.price} stock={p.stock}")
        elif cmd == "sell":
            try:
                pid = input("product id: ").strip()
                qty = int(input("quantity: "))
                tx = sell_product(user, pid, qty)
                print("Sold. Transaction id:", tx.id)
            except Exception as e:
                print("Error:", e)
        elif cmd == "purchase":
            try:
                pid = input("product id: ").strip()
                qty = int(input("quantity: "))
                price = input("unit price (or leave blank): ").strip()
                price = float(price) if price else None
                tx = purchase_product(user, pid, qty, price)
                print("Purchased. Transaction id:", tx.id)
            except Exception as e:
                print("Error:", e)
        elif cmd == "adduser" and user.role == "admin":
            uname = input("username: ").strip()
            pwd = input("password: ")
            role = input("role (admin/seller/purchaser/employee): ").strip() or "employee"
            try:
                create_user(uname, pwd, role=role)
                print("User created")
            except Exception as e:
                print("Error:", e)
        elif cmd == "edituser" and user.role == "admin":
            uname = input("username to edit: ").strip()
            newrole = input("new role (leave blank to keep): ").strip()
            newpwd = input("new password (leave blank to keep): ")
            from .auth import update_user
            fields = {}
            if newrole:
                fields["role"] = newrole
            if newpwd:
                fields["password"] = newpwd
            try:
                update_user(uname, **fields)
                print("User updated")
            except Exception as e:
                print("Error:", e)
        elif cmd == "report":
            path = generate_report()
            print("Report generated:", path)
        else:
            print("Unknown command")


def main():
    print("Welcome to Sem_LO2 - CLI")
    while True:
        username = input("username: ").strip()
        password = input("password: ")
        user = authenticate(username, password)
        if user:
            repl(user)
            break
        else:
            print("Invalid credentials. Try again or type 'exit' as username to quit.")
            if username.lower() == "exit":
                break


if __name__ == "__main__":
    main()
