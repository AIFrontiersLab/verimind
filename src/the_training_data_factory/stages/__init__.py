"""Role implementations. Components specialise one of these strategies."""

from the_training_data_factory.stages.answer import AnswerStage
from the_training_data_factory.stages.approval import ApprovalStage
from the_training_data_factory.stages.audit import AuditStage
from the_training_data_factory.stages.base import Stage, StageServices
from the_training_data_factory.stages.budget import BudgetStage
from the_training_data_factory.stages.cache import CacheStage
from the_training_data_factory.stages.enrich import EnrichStage
from the_training_data_factory.stages.fallback import FallbackStage
from the_training_data_factory.stages.ingest import IngestStage
from the_training_data_factory.stages.policy import PolicyStage
from the_training_data_factory.stages.retrieve import RetrieveStage
from the_training_data_factory.stages.score import ScoreStage

ROLE_CLASSES: dict[str, type[Stage]] = {
    "ingest": IngestStage,
    "retrieve": RetrieveStage,
    "enrich": EnrichStage,
    "score": ScoreStage,
    "cache": CacheStage,
    "policy": PolicyStage,
    "budget": BudgetStage,
    "approval": ApprovalStage,
    "fallback": FallbackStage,
    "audit": AuditStage,
    "answer": AnswerStage,
}

__all__ = ["ROLE_CLASSES", "Stage", "StageServices", *[cls.__name__ for cls in ROLE_CLASSES.values()]]
