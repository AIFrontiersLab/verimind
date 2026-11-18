# Lexical Search Engine

Blends upstream prior scores with query-aware relevance and reorders candidates.

| Property | Value |
|---|---|
| Stage | `lexical_search_engine` |
| Role | `score` |
| Interface | `process(ctx) -> None` |
| Critical | no |
| Source | `src/the_training_data_factory/components/lexical_search_engine/` |
| Tests | `tests/unit/components/test_component_lexical_search_engine.py` |

## Behaviour

Blends upstream prior scores with query-aware relevance and reorders candidates.

## Contract

- Input is bounded by `max_input_candidates`.
- Output contains no duplicate ids.
- Never introduces candidate ids that were not in its input.
- Output is sorted by descending score.

## On failure

Run degrades; fallback restores upstream prior order.

## Metrics

- `component_lexical_search_engine_runs_total`
- `component_lexical_search_engine_candidates_out` (histogram)
- `component_lexical_search_engine_removed_total`
