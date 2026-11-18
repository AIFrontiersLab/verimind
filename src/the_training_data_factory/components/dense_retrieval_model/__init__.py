"""Dense Retrieval Model.

Blends upstream prior scores with query-aware relevance and reorders candidates.
"""

from the_training_data_factory.components.dense_retrieval_model.adapter import ROLE, build
from the_training_data_factory.components.dense_retrieval_model.config import CONFIG, DenseRetrievalModelConfig
from the_training_data_factory.components.dense_retrieval_model.errors import DenseRetrievalModelError
from the_training_data_factory.components.dense_retrieval_model.service import DenseRetrievalModelService

__all__ = ["CONFIG", "ROLE", "build", "DenseRetrievalModelConfig", "DenseRetrievalModelError", "DenseRetrievalModelService"]
