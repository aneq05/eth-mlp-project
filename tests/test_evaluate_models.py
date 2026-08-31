import tempfile
from pathlib import Path
from unittest import TestCase

import pandas as pd

from src.pipelines.evaluate_models import evaluate_saved_predictions


class TestEvaluateSavedPredictions(TestCase):
    def test_evaluates_only_predictions_from_run_dir(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            legacy_predictions = root / "reports" / "predictions"
            run_predictions = root / "reports" / "runs" / "run_a" / "predictions"
            legacy_predictions.mkdir(parents=True)
            run_predictions.mkdir(parents=True)

            pd.DataFrame({"y_true": [0, 1], "y_pred": [0, 1]}).to_csv(
                legacy_predictions / "legacy_predictions.csv",
                index=False,
            )
            pd.DataFrame({"y_true": [0, 1, 2], "y_pred": [0, 1, 1]}).to_csv(
                run_predictions / "model_rank_1_predictions.csv",
                index=False,
            )

            report = evaluate_saved_predictions(root, run_dir=root / "reports" / "runs" / "run_a", make_figures=False)

            self.assertEqual(list(report.keys()), ["model_rank_1_predictions"])
            self.assertTrue((root / "reports" / "runs" / "run_a" / "evaluation_report.json").exists())
            self.assertFalse((root / "reports" / "evaluation_report.json").exists())

    def test_evaluation_can_generate_figures_with_headless_backend(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            run_dir = root / "reports" / "runs" / "run_a"
            predictions = run_dir / "predictions"
            predictions.mkdir(parents=True)
            pd.DataFrame({"y_true": [0, 1, 2], "y_pred": [0, 1, 1]}).to_csv(
                predictions / "ensemble_predictions.csv",
                index=False,
            )

            evaluate_saved_predictions(root, run_dir=run_dir, make_figures=True)

            self.assertTrue((run_dir / "figures" / "ensemble_predictions_confusion_matrix.png").exists())
