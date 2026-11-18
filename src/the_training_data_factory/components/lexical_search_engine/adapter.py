"""Port and registry adapter for Lexical Search Engine.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from the_training_data_factory.components.lexical_search_engine.config import CONFIG
from the_training_data_factory.components.lexical_search_engine.service import LexicalSearchEngineService
from the_training_data_factory.domain.models import PipelineContext

ROLE = CONFIG.role


class LexicalSearchEnginePort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> LexicalSearchEngineService:
    return LexicalSearchEngineService(services)
