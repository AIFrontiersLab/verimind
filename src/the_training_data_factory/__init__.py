"""The Training Data Factory: governed reference service.

Turn raw documents into auditable training datasets.

Public entry points:

* ``build_container`` - wire the full object graph from settings.
* ``run`` - execute a single request and return the outcome as a dict.
"""

from the_training_data_factory.application.pipeline import run
from the_training_data_factory.container import build_container
from the_training_data_factory.version import __version__

__all__ = ["__version__", "build_container", "run"]
