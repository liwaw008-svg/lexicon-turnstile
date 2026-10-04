# Lexicon Turnstile

## ADMISSION SLIP

`label presented -> meaning inspected -> one vocabulary slot chosen`

A shared vocabulary decays when synonyms masquerade as new concepts or familiar words quietly acquire incompatible constraints. Lexicon Turnstile makes admission a semantic operation rather than a spelling check.

The owner pins a public charter and names a separate auditor. A proposer supplies a definition from another origin. During review, validators fetch the charter, the candidate, and every canonical definition. They agree on only two bounded fields: `relation` and `matched_term_id`. The contract admits `UNIQUE` as `CANONICAL`, routes equivalent meaning to `ALIAS`, and isolates incompatible reuse as `CONFLICT`.

```text
PENDING -> CANONICAL
        -> ALIAS
        -> CONFLICT -> PENDING (one same-origin revision)
        -> EXPIRED  (permissionless after the review deadline)
```

Every decision preserves byte digests for the charter, candidate, and matched definition. The registry holds at most eight proposals so validator work stays bounded. The demo sources and wallets are operator-controlled; host separation proves source-slot enforcement, not institutional independence.

## Bench card

```text
$env:PYTHONIOENCODING='utf-8'; genvm-lint contracts/contract.py
python -m pytest -q
python scripts/deploy.py
python scripts/smoke.py
```

`deployment.json` and `network-run.json` are produced only after finalized successful StudioNet receipts.
