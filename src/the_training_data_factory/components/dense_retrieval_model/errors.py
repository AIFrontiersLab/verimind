"""Errors raised by Dense Retrieval Model. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from the_training_data_factory.kernel.errors import StageError


class DenseRetrievalModelError(StageError):
    code = "dense_retrieval_model_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("dense_retrieval_model", message, retryable=retryable, details=details)


class DenseRetrievalModelContractViolation(DenseRetrievalModelError):
    code = "dense_retrieval_model_contract_violation"
