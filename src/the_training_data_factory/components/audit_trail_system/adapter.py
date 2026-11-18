"""Port and registry adapter for Audit Trail System.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from the_training_data_factory.components.audit_trail_system.config import CONFIG
from the_training_data_factory.components.audit_trail_system.service import AuditTrailSystemService
from the_training_data_factory.domain.models import PipelineContext

ROLE = CONFIG.role


class AuditTrailSystemPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> AuditTrailSystemService:
    return AuditTrailSystemService(services)
