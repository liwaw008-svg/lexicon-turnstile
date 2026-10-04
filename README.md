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

## Live stamp

StudioNet contract: `0xea84eB31d7d066731e2A9FaaaCB3f34Fca0be74a`

The recorded run admitted `RECOVERY-1791127237` as `CANONICAL`, then routed `RESTORE-1791127237` to `ALIAS` with the first term as its exact match. The alias review finalized successfully in transaction `0x0ddbb8100132824e0da2862ec581dc05280bb19089fc2a37246abbe632774d38`.

Replay and unauthorized review were also exercised live. Transaction `0x33c2bc7dcdba4c9fb7aab2873e032db8f9483e3a10fc03af6d5990b2e5b201ca` finalized with the expected contract `ERROR`, rather than altering the canonical record.

## Bench card

```text
$env:PYTHONIOENCODING='utf-8'; genvm-lint contracts/contract.py
python -m pytest -q
python scripts/deploy.py
python scripts/smoke.py
```

`deployment.json` and `network-run.json` are produced only after finalized successful StudioNet receipts.

`negative-run.json` records a finalized expected rejection. `contribution-manifest.json` binds the reviewed source commit and digest to the deployment and evidence files.
