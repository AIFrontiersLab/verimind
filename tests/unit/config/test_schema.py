import pytest

from the_training_data_factory.config.schema import validate_settings
from the_training_data_factory.config.settings import Settings
from the_training_data_factory.kernel.errors import ConfigurationError


@pytest.mark.parametrize(
    "mutate",
    [
        lambda s: setattr(s.pipeline, "top_k", 0),
        lambda s: setattr(s.pipeline, "prior_weight", 1.5),
        lambda s: setattr(s.pipeline, "stages", []),
        lambda s: setattr(s.resilience, "bulkhead_limit", 0),
        lambda s: setattr(s.governance, "default_clearance", "secret"),
        lambda s: setattr(s.budget, "default_tokens", 10**9),
        lambda s: setattr(s.storage, "backend", "postgres"),
    ],
)
def test_invalid_settings_rejected(mutate):
    settings = Settings()
    mutate(settings)
    with pytest.raises(ConfigurationError):
        validate_settings(settings)


def test_defaults_are_valid():
    validate_settings(Settings())
