"""Static configuration for the Audit Trail System component."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AuditTrailSystemConfig:
    name: str = "audit_trail_system"
    display_name: str = 'Audit Trail System'
    role: str = "audit"
    interface: str = 'process(ctx) -> None'
    responsibility: str = 'Appends an immutable, redacted audit record of what the run saw and decided.'
    max_input_candidates: int = 10_000
    may_introduce_ids: bool = False
    enforce_sorted_output: bool = False


CONFIG = AuditTrailSystemConfig()
