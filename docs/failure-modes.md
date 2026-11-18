# Failure modes

## From the design specification

- None listed.

## Per stage

| Stage | Role | Behaviour on failure |
|---|---|---|
| `intake` | `ingest` | Run fails; the request never reaches retrieval. |
| `corpus_retrieval` | `retrieve` | Run degrades; supplied candidates (if any) continue. |
| `signal_enricher` | `enrich` | Run degrades; candidates continue without annotations. |
| `ranking_cache` | `cache` | Run degrades; the request is treated as a cache miss. |
| `lexical_search_engine` | `score` | Run degrades; fallback restores upstream prior order. |
| `dense_retrieval_model` | `score` | Run degrades; fallback restores upstream prior order. |
| `score_fusion_module` | `score` | Run degrades; fallback restores upstream prior order. |
| `graceful_fallback` | `fallback` | Run degrades; ordering from the last healthy stage is kept. |
| `access_policy` | `policy` | Run fails closed: no candidates survive, the run abstains with `policy_unavailable`. |
| `audit_trail_system` | `audit` | Run degrades; the answer is still returned and the gap is visible in metrics. |
| `answer_assembly` | `answer` | Run fails with `stage_failure:<name>`. |

## Platform

| Condition | Behaviour |
|---|---|
| Bulkhead full | 503 `stage_error` |
| Rate limited | 429 `budget_exceeded` |
| Breaker open | stage reported `degraded` with `circuit_open`; `/readyz` fails |
| Hook raises | captured in `hooks.failures`; run continues |
| Event handler raises | captured in `dead_letters`; run continues |
