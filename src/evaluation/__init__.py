from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .metrics import compute_classification_metrics
    from .statistical_tests import bootstrap_metric_difference


def __getattr__(name: str):
    if name == "compute_classification_metrics":
        from .metrics import compute_classification_metrics

        return compute_classification_metrics
    if name == "bootstrap_metric_difference":
        from .statistical_tests import bootstrap_metric_difference

        return bootstrap_metric_difference
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "bootstrap_metric_difference",
    "compute_classification_metrics",
]
