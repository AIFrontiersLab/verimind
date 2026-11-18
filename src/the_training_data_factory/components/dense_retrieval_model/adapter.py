"""Port and registry adapter for Dense Retrieval Model.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from the_training_data_factory.components.dense_retrieval_model.config import CONFIG
from the_training_data_factory.components.dense_retrieval_model.service import DenseRetrievalModelService
from the_training_data_factory.domain.models import PipelineContext

ROLE = CONFIG.role


class DenseRetrievalModelPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> DenseRetrievalModelService:
    return DenseRetrievalModelService(services)
