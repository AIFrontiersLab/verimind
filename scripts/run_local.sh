#!/usr/bin/env bash
set -euo pipefail
export THE_TRAINING_DATA_FACTORY_CONFIG=${THE_TRAINING_DATA_FACTORY_CONFIG:-config/development.toml}
PYTHONPATH=src exec python -m the_training_data_factory serve "$@"
