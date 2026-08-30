from unittest import TestCase

import numpy as np

from src.evaluation.statistical_tests import bootstrap_metric_difference


class TestBootstrapMetricDifference(TestCase):
    def test_returns_block_size_for_block_bootstrap(self) -> None:
        y_true = np.array([0, 1, 1, 2, 2, 0])
        y_pred_a = np.array([0, 1, 0, 2, 1, 0])
        y_pred_b = np.array([1, 1, 0, 2, 2, 0])

        result = bootstrap_metric_difference(
            y_true=y_true,
            y_pred_a=y_pred_a,
            y_pred_b=y_pred_b,
            metric_fn=lambda yt, yp: float(np.mean(yt == yp)),
            n_bootstrap=10,
            random_state=7,
            block_size=3,
        )

        self.assertEqual(result["block_size"], 3)
        self.assertIn("mean_diff", result)

    def test_rejects_invalid_block_size(self) -> None:
        y = np.array([0, 1])

        with self.assertRaisesRegex(ValueError, "positive integer"):
            bootstrap_metric_difference(
                y_true=y,
                y_pred_a=y,
                y_pred_b=y,
                metric_fn=lambda yt, yp: float(np.mean(yt == yp)),
                block_size=0,
            )
