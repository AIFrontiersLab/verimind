"""Score Fusion Module.

Blends upstream prior scores with query-aware relevance and reorders candidates.
"""

from the_training_data_factory.components.score_fusion_module.adapter import ROLE, build
from the_training_data_factory.components.score_fusion_module.config import CONFIG, ScoreFusionModuleConfig
from the_training_data_factory.components.score_fusion_module.errors import ScoreFusionModuleError
from the_training_data_factory.components.score_fusion_module.service import ScoreFusionModuleService

__all__ = ["CONFIG", "ROLE", "build", "ScoreFusionModuleConfig", "ScoreFusionModuleError", "ScoreFusionModuleService"]
