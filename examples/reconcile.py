from decimal import Decimal

from tideway.ledger import Ledger, Posting

ledger = Ledger()
ledger.add("close-2026-08", [
    Posting("cash", Decimal("4200.00")),
    Posting("revenue", Decimal("-4000.00")),
    Posting("fx-gain", Decimal("-200.00")),
])
ledger.assert_balanced("close-2026-08")
print("cash balance:", ledger.balance("cash"))
