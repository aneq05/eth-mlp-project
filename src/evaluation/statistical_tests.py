from collections.abc import Callable

import numpy as np


def bootstrap_metric_difference(
    y_true: np.ndarray,
    y_pred_a: np.ndarray,
    y_pred_b: np.ndarray,
    metric_fn: Callable[[np.ndarray, np.ndarray], float],
    n_bootstrap: int = 1000,
    random_state: int = 42,
) -> dict[str, float]:
    rng = np.random.default_rng(random_state)
    n = len(y_true)
    diffs = []

    for _ in range(n_bootstrap):
        idx = rng.integers(0, n, size=n)
        score_a = metric_fn(y_true[idx], y_pred_a[idx])
        score_b = metric_fn(y_true[idx], y_pred_b[idx])
        diffs.append(score_a - score_b)

    diffs_arr = np.array(diffs)
    return {
        "mean_diff": float(np.mean(diffs_arr)),
        "ci_lower_95": float(np.quantile(diffs_arr, 0.025)),
        "ci_upper_95": float(np.quantile(diffs_arr, 0.975)),
    }
