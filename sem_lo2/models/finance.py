"""Finance model: balance and transaction history"""

from dataclasses import dataclass, field
from typing import List
import time
import uuid


@dataclass
class Transaction:
    id: str
    kind: str  # sale / purchase / adjustment
    amount: float
    by_user: str
    details: str
    timestamp: float

    def to_dict(self):
        return {"id": self.id, "kind": self.kind, "amount": self.amount, "by_user": self.by_user, "details": self.details, "timestamp": self.timestamp}

    @staticmethod
    def create(kind, amount, by_user, details=""):
        return Transaction(id=str(uuid.uuid4()), kind=kind, amount=amount, by_user=by_user, details=details, timestamp=time.time())


@dataclass
class Finance:
    balance: float = 0.0
    transactions: List[Transaction] = field(default_factory=list)

    def apply(self, transaction: Transaction):
        self.transactions.append(transaction)
        self.balance += transaction.amount

    def to_dict(self):
        return {"balance": self.balance, "transactions": [t.to_dict() for t in self.transactions]}

    @staticmethod
    def from_dict(d):
        txs = []
        for t in d.get("transactions", []):
            txs.append(Transaction(id=t["id"], kind=t["kind"], amount=float(t["amount"]), by_user=t.get("by_user",""), details=t.get("details",""), timestamp=float(t.get("timestamp",0))))
        return Finance(balance=float(d.get("balance",0.0)), transactions=txs)
