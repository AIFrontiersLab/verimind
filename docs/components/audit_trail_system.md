# Audit Trail System

Appends an immutable, redacted audit record of what the run saw and decided.

| Property | Value |
|---|---|
| Stage | `audit_trail_system` |
| Role | `audit` |
| Interface | `process(ctx) -> None` |
| Critical | no |
| Source | `src/the_training_data_factory/components/audit_trail_system/` |
| Tests | `tests/unit/components/test_component_audit_trail_system.py` |

## Behaviour

Appends an immutable, redacted audit record of what the run saw and decided.

## Contract

- Input is bounded by `max_input_candidates`.
- Output contains no duplicate ids.
- Never introduces candidate ids that were not in its input.
- Ordering is preserved or intentionally changed per role.

## On failure

Run degrades; the answer is still returned and the gap is visible in metrics.

## Metrics

- `component_audit_trail_system_runs_total`
- `component_audit_trail_system_candidates_out` (histogram)
- `component_audit_trail_system_removed_total`
