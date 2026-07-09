"""Authentication and user management (JSON storage)"""

import os
import hashlib
import binascii
from typing import List
from .models.user import User, Admin, Employee
from .storage import load_json, save_json

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
USERS_PATH = os.path.join(DATA_DIR, "users.json")


def _hash_password(password: str, salt: bytes = None) -> str:
    # Simple salted SHA256: store as hex(salt)$hex(hash)
    if salt is None:
        salt = os.urandom(16)
    hash_bytes = hashlib.sha256(salt + password.encode("utf-8")).digest()
    return binascii.hexlify(salt).decode() + "$" + binascii.hexlify(hash_bytes).decode()


def _verify_password(password: str, stored: str) -> bool:
    try:
        salt_hex, hash_hex = stored.split("$")
        salt = binascii.unhexlify(salt_hex)
        h = hashlib.sha256(salt + password.encode("utf-8")).digest()
        return binascii.hexlify(h).decode() == hash_hex
    except Exception:
        return False


def load_users() -> List[User]:
    data = load_json(USERS_PATH) or {"users": []}
    users = [User.from_dict(u) for u in data.get("users", [])]
    return users


def save_users(users: List[User]):
    data = {"users": [u.to_dict() for u in users]}
    save_json(USERS_PATH, data)


def find_user(username: str):
    users = load_users()
    for u in users:
        if u.username == username:
            return u
    return None


def create_user(username: str, password: str, role: str = "employee") -> User:
    users = load_users()
    if any(u.username == username for u in users):
        raise ValueError("User exists")
    u = User(id=None, username=username, password_hash=_hash_password(password), role=role)
    # ensure id set
    if not u.id:
        import uuid
        u.id = str(uuid.uuid4())
    users.append(u)
    save_users(users)
    return u


def authenticate(username: str, password: str):
    u = find_user(username)
    if not u:
        return None
    if _verify_password(password, u.password_hash):
        return u
    return None


def update_user(username: str, **fields):
    users = load_users()
    for i, u in enumerate(users):
        if u.username == username:
            for k, v in fields.items():
                if k == "password":
                    u.password_hash = _hash_password(v)
                elif k in ("username", "role"):
                    setattr(u, k, v)
                else:
                    u.extra[k] = v
            users[i] = u
            save_users(users)
            return u
    raise ValueError("User not found")
