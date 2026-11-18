"""Event publication port."""

from __future__ import annotations

from typing import Callable, Protocol

from the_training_data_factory.kernel.events import DomainEvent


class EventBus(Protocol):
    def publish(self, event: DomainEvent) -> None: ...

    def subscribe(self, name: str, handler: Callable[[DomainEvent], None]) -> None: ...
