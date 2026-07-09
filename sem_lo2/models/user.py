"""User models with simple inheritance"""

import uuid
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class User:
    id: str
    username: str
    password_hash: str
    role: str = "employee"
    extra: Dict = field(default_factory=dict)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password_hash": self.password_hash,
            "role": self.role,
            "extra": self.extra,
        }

    @staticmethod
    def from_dict(d):
        return User(
            id=d.get("id") or str(uuid.uuid4()),
            username=d["username"],
            password_hash=d["password_hash"],
            role=d.get("role", "employee"),
            extra=d.get("extra", {}),
        )


class Admin(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.role = "admin"


class Employee(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.role = kwargs.get("role", "employee")
