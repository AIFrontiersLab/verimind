import pytest

from the_training_data_factory.domain import events


def test_event_factory_validates_names():
    evt = events.event(events.RUN_STARTED, "run_1", tenant="acme")
    assert evt.to_dict()["payload"] == {"tenant": "acme"}
    with pytest.raises(ValueError):
        events.event("made.up", "run_1")
