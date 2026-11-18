# Dense Retrieval Model

Blends upstream prior scores with query-aware relevance and reorders candidates.

| Property | Value |
|---|---|
| Stage | `dense_retrieval_model` |
| Role | `score` |
| Interface | `process(ctx) -> None` |
| Critical | no |
| Source | `src/the_training_data_factory/components/dense_retrieval_model/` |
| Tests | `tests/unit/components/test_component_dense_retrieval_model.py` |

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

- `component_dense_retrieval_model_runs_total`
- `component_dense_retrieval_model_candidates_out` (histogram)
- `component_dense_retrieval_model_removed_total`
