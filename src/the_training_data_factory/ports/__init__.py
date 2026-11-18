"""Ports: the interfaces the application core requires from the outside world.

Adapters under ``the_training_data_factory.adapters`` implement these protocols. The core never
imports an adapter directly; the composition root (``container.py``) wires them.
"""

from the_training_data_factory.ports.audit import AuditSink
from the_training_data_factory.ports.cache import RankingCache
from the_training_data_factory.ports.corpus import CorpusRepository
from the_training_data_factory.ports.event_bus import EventBus
from the_training_data_factory.ports.repository import RunRepository
from the_training_data_factory.ports.scorer import RelevanceScorer

__all__ = ["AuditSink", "CorpusRepository", "EventBus", "RankingCache", "RelevanceScorer", "RunRepository"]
