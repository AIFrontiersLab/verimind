"""Extension points: stage factories and lifecycle hooks."""

from the_training_data_factory.plugins.hooks import HookManager
from the_training_data_factory.plugins.registry import StageRegistry

__all__ = ["HookManager", "StageRegistry"]
