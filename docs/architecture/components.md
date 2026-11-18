# Components (C4 level 3)

| # | Stage | Role | Critical | Source |
|---|---|---|---|---|
| 1 | `intake` (Intake) | `ingest` | yes | built-in |
| 2 | `corpus_retrieval` (Corpus Retrieval) | `retrieve` | no | built-in |
| 3 | `signal_enricher` (Signal Enricher) | `enrich` | no | [component](../components/signal_enricher.md) |
| 4 | `ranking_cache` (Ranking Cache) | `cache` | no | [component](../components/ranking_cache.md) |
| 5 | `lexical_search_engine` (Lexical Search Engine) | `score` | no | [component](../components/lexical_search_engine.md) |
| 6 | `dense_retrieval_model` (Dense Retrieval Model) | `score` | no | [component](../components/dense_retrieval_model.md) |
| 7 | `score_fusion_module` (Score Fusion Module) | `score` | no | [component](../components/score_fusion_module.md) |
| 8 | `graceful_fallback` (Graceful Fallback) | `fallback` | no | built-in |
| 9 | `access_policy` (Access Policy) | `policy` | yes | built-in |
| 10 | `audit_trail_system` (Audit Trail System) | `audit` | no | [component](../components/audit_trail_system.md) |
| 11 | `answer_assembly` (Answer Assembly) | `answer` | yes | built-in |

Each concept component follows the same internal layout so reviewers can navigate
any of them blind: `config.py`, `port.py`, `service.py`, `validators.py`, `models.py`,
`metrics.py`, `errors.py`, `adapter.py`.
