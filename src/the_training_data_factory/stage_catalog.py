"""Stage catalog for The Training Data Factory.

Declares the default stage order and registers every built-in and component stage
with the plugin registry. Imports of stage classes are deferred so configuration
modules can read ``DEFAULT_STAGE_ORDER`` without import cycles.
"""

from __future__ import annotations

DEFAULT_STAGE_ORDER = [
    "intake",
    "corpus_retrieval",
    "signal_enricher",
    "ranking_cache",
    "lexical_search_engine",
    "dense_retrieval_model",
    "score_fusion_module",
    "graceful_fallback",
    "access_policy",
    "audit_trail_system",
    "answer_assembly",
]

BUILTINS = {
    "intake": "ingest",
    "corpus_retrieval": "retrieve",
    "relevance_scoring": "score",
    "access_policy": "policy",
    "graceful_fallback": "fallback",
    "answer_assembly": "answer",
}

COMPONENTS = [
    {"name": 'Lexical Search Engine', "slug": "lexical_search_engine", "role": "score", "origin": "spec"},
    {"name": 'Dense Retrieval Model', "slug": "dense_retrieval_model", "role": "score", "origin": "spec"},
    {"name": 'Score Fusion Module', "slug": "score_fusion_module", "role": "score", "origin": "spec"},
    {"name": 'Audit Trail System', "slug": "audit_trail_system", "role": "audit", "origin": "spec"},
    {"name": 'Signal Enricher', "slug": "signal_enricher", "role": "enrich", "origin": "padded"},
    {"name": 'Ranking Cache', "slug": "ranking_cache", "role": "cache", "origin": "padded"},
]


def register_all(registry) -> None:
    from the_training_data_factory.components import COMPONENT_FACTORIES
    from the_training_data_factory.stages import ROLE_CLASSES

    for name, role in BUILTINS.items():
        cls = ROLE_CLASSES[role]
        registry.register(name, role, lambda services, cls=cls, name=name: cls(name, services), source="builtin")
    for name, (role, factory) in COMPONENT_FACTORIES.items():
        registry.register(name, role, factory, source="component")
