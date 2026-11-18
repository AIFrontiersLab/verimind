"""Concept-specific components. Each one specialises a stage role with its own
configuration, validation, metrics, and errors."""

from the_training_data_factory.components.audit_trail_system import adapter as _audit_trail_system
from the_training_data_factory.components.dense_retrieval_model import adapter as _dense_retrieval_model
from the_training_data_factory.components.lexical_search_engine import adapter as _lexical_search_engine
from the_training_data_factory.components.ranking_cache import adapter as _ranking_cache
from the_training_data_factory.components.score_fusion_module import adapter as _score_fusion_module
from the_training_data_factory.components.signal_enricher import adapter as _signal_enricher

COMPONENT_FACTORIES = {
    "lexical_search_engine": (_lexical_search_engine.ROLE, _lexical_search_engine.build),
    "dense_retrieval_model": (_dense_retrieval_model.ROLE, _dense_retrieval_model.build),
    "score_fusion_module": (_score_fusion_module.ROLE, _score_fusion_module.build),
    "audit_trail_system": (_audit_trail_system.ROLE, _audit_trail_system.build),
    "signal_enricher": (_signal_enricher.ROLE, _signal_enricher.build),
    "ranking_cache": (_ranking_cache.ROLE, _ranking_cache.build),
}
