"""Pre- and post-conditions for Audit Trail System.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from the_training_data_factory.components.audit_trail_system.config import AuditTrailSystemConfig
from the_training_data_factory.components.audit_trail_system.errors import AuditTrailSystemContractViolation
from the_training_data_factory.components.audit_trail_system.models import AuditTrailSystemInput


def validate_input(ctx, config: AuditTrailSystemConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise AuditTrailSystemContractViolation(
            "too many candidates for audit_trail_system",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: AuditTrailSystemInput, config: AuditTrailSystemConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise AuditTrailSystemContractViolation("duplicate candidate ids after audit_trail_system")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise AuditTrailSystemContractViolation(
                "audit_trail_system introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise AuditTrailSystemContractViolation("audit_trail_system produced an unsorted ranking")
