"""Static configuration for the Lexical Search Engine component."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LexicalSearchEngineConfig:
    name: str = "lexical_search_engine"
    display_name: str = 'Lexical Search Engine'
    role: str = "score"
    interface: str = 'process(ctx) -> None'
    responsibility: str = 'Blends upstream prior scores with query-aware relevance and reorders candidates.'
    max_input_candidates: int = 10_000
    may_introduce_ids: bool = False
    enforce_sorted_output: bool = True


CONFIG = LexicalSearchEngineConfig()
