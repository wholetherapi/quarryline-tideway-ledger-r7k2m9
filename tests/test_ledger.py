from decimal import Decimal

from tideway.ledger import Ledger, Posting


def test_simple_balance():
    ledger = Ledger()
    ledger.add("tx-1", [Posting("cash", Decimal("100")), Posting("revenue", Decimal("-100"))])
    assert ledger.balance("cash") == Decimal("100")
    ledger.assert_balanced("tx-1")
