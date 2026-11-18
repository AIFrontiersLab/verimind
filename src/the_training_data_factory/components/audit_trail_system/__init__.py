"""Audit Trail System.

Appends an immutable, redacted audit record of what the run saw and decided.
"""

from the_training_data_factory.components.audit_trail_system.adapter import ROLE, build
from the_training_data_factory.components.audit_trail_system.config import CONFIG, AuditTrailSystemConfig
from the_training_data_factory.components.audit_trail_system.errors import AuditTrailSystemError
from the_training_data_factory.components.audit_trail_system.service import AuditTrailSystemService

__all__ = ["CONFIG", "ROLE", "build", "AuditTrailSystemConfig", "AuditTrailSystemError", "AuditTrailSystemService"]
