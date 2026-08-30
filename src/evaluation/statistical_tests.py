from collections.abc import Callable

import numpy as np


def bootstrap_metric_difference(
    y_true: np.ndarray,
    y_pred_a: np.ndarray,
    y_pred_b: np.ndarray,
    metric_fn: Callable[[np.ndarray, np.ndarray], float],
    n_bootstrap: int = 1000,
    random_state: int = 42,
    block_size: int = 1,
) -> dict[str, float]:
    if block_size <= 0:
        raise ValueError("block_size must be a positive integer")

    rng = np.random.default_rng(random_state)
    n = len(y_true)
    diffs = []

    for _ in range(n_bootstrap):
        if block_size == 1:
            idx = rng.integers(0, n, size=n)
        else:
            starts = rng.integers(0, max(1, n - block_size + 1), size=int(np.ceil(n / block_size)))
            idx = np.concatenate([np.arange(start, min(start + block_size, n)) for start in starts])[:n]

        score_a = metric_fn(y_true[idx], y_pred_a[idx])
        score_b = metric_fn(y_true[idx], y_pred_b[idx])
        diffs.append(score_a - score_b)

    diffs_arr = np.array(diffs)
    return {
        "mean_diff": float(np.mean(diffs_arr)),
        "ci_lower_95": float(np.quantile(diffs_arr, 0.025)),
        "ci_upper_95": float(np.quantile(diffs_arr, 0.975)),
        "block_size": int(block_size),
    }
