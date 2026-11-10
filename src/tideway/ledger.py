"""Core ledger model and reconciliation helpers."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable


@dataclass(frozen=True)
class Posting:
    """A single debit or credit posting."""

    account: str
    amount: Decimal
    currency: str = "USD"

    def signed(self) -> Decimal:
        return self.amount


class Ledger:
    """An append-only collection of postings grouped by transaction."""

    def __init__(self) -> None:
        self._postings: dict[str, list[Posting]] = {}

    def add(self, transaction_id: str, postings: Iterable[Posting]) -> None:
        bucket = self._postings.setdefault(transaction_id, [])
        bucket.extend(postings)

    def balance(self, account: str) -> Decimal:
        total = Decimal("0")
        for postings in self._postings.values():
            for posting in postings:
                if posting.account == account:
                    total += posting.signed()
        return total

    def assert_balanced(self, transaction_id: str) -> None:
        total = sum((p.signed() for p in self._postings.get(transaction_id, [])), Decimal("0"))
        if total != Decimal("0"):
            raise ValueError(f"transaction {transaction_id} is unbalanced: {total}")
