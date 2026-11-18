"""Typed configuration: defaults in code, profiles in TOML, overrides from the environment."""

from the_training_data_factory.config.loader import load_settings
from the_training_data_factory.config.settings import Settings

__all__ = ["Settings", "load_settings"]
