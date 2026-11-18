"""Static configuration for the Dense Retrieval Model component."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DenseRetrievalModelConfig:
    name: str = "dense_retrieval_model"
    display_name: str = 'Dense Retrieval Model'
    role: str = "score"
    interface: str = 'process(ctx) -> None'
    responsibility: str = 'Blends upstream prior scores with query-aware relevance and reorders candidates.'
    max_input_candidates: int = 10_000
    may_introduce_ids: bool = False
    enforce_sorted_output: bool = True


CONFIG = DenseRetrievalModelConfig()
