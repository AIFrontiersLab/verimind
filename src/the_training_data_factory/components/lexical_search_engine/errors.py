"""Errors raised by Lexical Search Engine. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from the_training_data_factory.kernel.errors import StageError


class LexicalSearchEngineError(StageError):
    code = "lexical_search_engine_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("lexical_search_engine", message, retryable=retryable, details=details)


class LexicalSearchEngineContractViolation(LexicalSearchEngineError):
    code = "lexical_search_engine_contract_violation"
