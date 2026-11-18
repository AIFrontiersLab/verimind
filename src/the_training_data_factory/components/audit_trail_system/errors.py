"""Errors raised by Audit Trail System. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from the_training_data_factory.kernel.errors import StageError


class AuditTrailSystemError(StageError):
    code = "audit_trail_system_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("audit_trail_system", message, retryable=retryable, details=details)


class AuditTrailSystemContractViolation(AuditTrailSystemError):
    code = "audit_trail_system_contract_violation"
