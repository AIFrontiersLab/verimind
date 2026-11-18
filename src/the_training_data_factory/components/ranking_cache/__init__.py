"""Ranking Cache.

Short-circuits repeated identical requests with a TTL-bounded ranking cache keyed by principal.
"""

from the_training_data_factory.components.ranking_cache.adapter import ROLE, build
from the_training_data_factory.components.ranking_cache.config import CONFIG, RankingCacheConfig
from the_training_data_factory.components.ranking_cache.errors import RankingCacheError
from the_training_data_factory.components.ranking_cache.service import RankingCacheService

__all__ = ["CONFIG", "ROLE", "build", "RankingCacheConfig", "RankingCacheError", "RankingCacheService"]
