"""Port and registry adapter for Signal Enricher.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from the_training_data_factory.components.signal_enricher.config import CONFIG
from the_training_data_factory.components.signal_enricher.service import SignalEnricherService
from the_training_data_factory.domain.models import PipelineContext

ROLE = CONFIG.role


class SignalEnricherPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> SignalEnricherService:
    return SignalEnricherService(services)
