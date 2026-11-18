"""Dense Retrieval Model service.

Role: ``score``. Blends upstream prior scores with query-aware relevance and reorders candidates.

Responsibility (from the architecture specification):
    Blends upstream prior scores with query-aware relevance and reorders candidates.

The service specialises :class:`ScoreStage` and wraps it with this
component's contract checks, metrics, and per-run report.
"""

from __future__ import annotations

from the_training_data_factory.components.dense_retrieval_model.config import CONFIG, DenseRetrievalModelConfig
from the_training_data_factory.components.dense_retrieval_model.models import DenseRetrievalModelInput, DenseRetrievalModelReport
from the_training_data_factory.components.dense_retrieval_model.validators import validate_input, validate_output
from the_training_data_factory.stages.score import ScoreStage

METRIC_PREFIX = "component_dense_retrieval_model"
RUNS = f"{METRIC_PREFIX}_runs_total"
CANDIDATES_OUT = f"{METRIC_PREFIX}_candidates_out"
REMOVED = f"{METRIC_PREFIX}_removed_total"


def record_metrics(metrics, report: DenseRetrievalModelReport) -> None:
    if metrics is None:
        return
    metrics.inc(RUNS)
    metrics.observe(CANDIDATES_OUT, report.candidates_out)
    if report.removed:
        metrics.inc(REMOVED, len(report.removed))


class DenseRetrievalModelService(ScoreStage):
    def __init__(self, services, config: DenseRetrievalModelConfig = CONFIG) -> None:
        super().__init__(config.name, services, description=config.responsibility)
        self.config = config

    def process(self, ctx) -> None:
        validate_input(ctx, self.config)
        before = DenseRetrievalModelInput.from_context(ctx)
        super().process(ctx)
        if ctx.halted and not ctx.candidates:
            report = DenseRetrievalModelReport.diff(self.name, before, [], halted=True)
        else:
            validate_output(ctx, before, self.config)
            report = DenseRetrievalModelReport.diff(self.name, before, [c.doc_id for c in ctx.candidates])
        ctx.metadata.setdefault("reports", {})[self.name] = report.to_dict()
        record_metrics(self.services.metrics, report)

    def describe(self) -> dict:
        info = super().describe()
        info.update({"display_name": self.config.display_name, "interface": self.config.interface})
        return info
