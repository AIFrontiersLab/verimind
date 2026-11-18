"""Every default adapter structurally satisfies the port it implements."""

import inspect

import pytest

from the_training_data_factory.adapters.outbound import (
    InMemoryAuditSink,
    InMemoryCorpus,
    InMemoryEventBus,
    InMemoryRunRepository,
    JsonlAuditSink,
    JsonlRunRepository,
    LexicalScorer,
    TTLRankingCache,
)
from the_training_data_factory.ports import AuditSink, CorpusRepository, EventBus, RankingCache, RelevanceScorer, RunRepository


def _methods(protocol):
    return {name for name, _ in inspect.getmembers(protocol, inspect.isfunction) if not name.startswith("_")}


@pytest.mark.parametrize(
    "port, adapter",
    [
        (RunRepository, InMemoryRunRepository),
        (RunRepository, JsonlRunRepository),
        (CorpusRepository, InMemoryCorpus),
        (RankingCache, TTLRankingCache),
        (EventBus, InMemoryEventBus),
        (RelevanceScorer, LexicalScorer),
        (AuditSink, InMemoryAuditSink),
        (AuditSink, JsonlAuditSink),
    ],
)
def test_adapter_implements_port(port, adapter):
    missing = {m for m in _methods(port) if not callable(getattr(adapter, m, None))}
    assert not missing, f"{adapter.__name__} missing {missing}"
