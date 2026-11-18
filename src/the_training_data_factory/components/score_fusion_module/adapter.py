"""Port and registry adapter for Score Fusion Module.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from the_training_data_factory.components.score_fusion_module.config import CONFIG
from the_training_data_factory.components.score_fusion_module.service import ScoreFusionModuleService
from the_training_data_factory.domain.models import PipelineContext

ROLE = CONFIG.role


class ScoreFusionModulePort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> ScoreFusionModuleService:
    return ScoreFusionModuleService(services)
