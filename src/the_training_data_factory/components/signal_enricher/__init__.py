"""Signal Enricher.

Annotates candidates with token counts and query overlap, and collapses duplicate passages.
"""

from the_training_data_factory.components.signal_enricher.adapter import ROLE, build
from the_training_data_factory.components.signal_enricher.config import CONFIG, SignalEnricherConfig
from the_training_data_factory.components.signal_enricher.errors import SignalEnricherError
from the_training_data_factory.components.signal_enricher.service import SignalEnricherService

__all__ = ["CONFIG", "ROLE", "build", "SignalEnricherConfig", "SignalEnricherError", "SignalEnricherService"]
