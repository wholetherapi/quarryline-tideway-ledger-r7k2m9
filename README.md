# Tideway Ledger

Companion implementation for the Tideway Ledger catalog item.

**Status: Released** — v1.2.0 (2026-08-19)

Tideway Ledger reconciles multi-currency journal entries and keeps a
deterministic audit trail for every close cycle.

## Features

- Double-entry reconciliation across account trees
- Replayable event log with stable ordering
- FX normalization using daily reference rates
- Balance assertions with readable diagnostics

## Layout

- `src/tideway/` — library code
- `tests/` — automated checks
- `examples/` — a runnable reconciliation sample

## Quick start

```bash
python -m pip install -e .
python examples/reconcile.py
```
