"""Pre- and post-conditions for Lexical Search Engine.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from the_training_data_factory.components.lexical_search_engine.config import LexicalSearchEngineConfig
from the_training_data_factory.components.lexical_search_engine.errors import LexicalSearchEngineContractViolation
from the_training_data_factory.components.lexical_search_engine.models import LexicalSearchEngineInput


def validate_input(ctx, config: LexicalSearchEngineConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise LexicalSearchEngineContractViolation(
            "too many candidates for lexical_search_engine",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: LexicalSearchEngineInput, config: LexicalSearchEngineConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise LexicalSearchEngineContractViolation("duplicate candidate ids after lexical_search_engine")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise LexicalSearchEngineContractViolation(
                "lexical_search_engine introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise LexicalSearchEngineContractViolation("lexical_search_engine produced an unsorted ranking")
