"""Lexical Search Engine.

Blends upstream prior scores with query-aware relevance and reorders candidates.
"""

from the_training_data_factory.components.lexical_search_engine.adapter import ROLE, build
from the_training_data_factory.components.lexical_search_engine.config import CONFIG, LexicalSearchEngineConfig
from the_training_data_factory.components.lexical_search_engine.errors import LexicalSearchEngineError
from the_training_data_factory.components.lexical_search_engine.service import LexicalSearchEngineService

__all__ = ["CONFIG", "ROLE", "build", "LexicalSearchEngineConfig", "LexicalSearchEngineError", "LexicalSearchEngineService"]
