"""Pre- and post-conditions for Dense Retrieval Model.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from the_training_data_factory.components.dense_retrieval_model.config import DenseRetrievalModelConfig
from the_training_data_factory.components.dense_retrieval_model.errors import DenseRetrievalModelContractViolation
from the_training_data_factory.components.dense_retrieval_model.models import DenseRetrievalModelInput


def validate_input(ctx, config: DenseRetrievalModelConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise DenseRetrievalModelContractViolation(
            "too many candidates for dense_retrieval_model",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: DenseRetrievalModelInput, config: DenseRetrievalModelConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise DenseRetrievalModelContractViolation("duplicate candidate ids after dense_retrieval_model")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise DenseRetrievalModelContractViolation(
                "dense_retrieval_model introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise DenseRetrievalModelContractViolation("dense_retrieval_model produced an unsorted ranking")
