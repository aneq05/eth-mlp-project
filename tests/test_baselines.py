import tempfile
from pathlib import Path
from unittest import TestCase

import numpy as np
import pandas as pd

from src.core.config import DataConfig
from src.pipelines.train_baselines import run_baseline_models


class TestBaselineModels(TestCase):
    def test_baselines_write_run_local_results(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            run_dir = Path(tmpdir)
            data_dir = run_dir / "data"
            data_dir.mkdir()
            config = DataConfig().with_run_dir(run_dir)

            def make_split(start: int, rows: int) -> pd.DataFrame:
                x = np.arange(start, start + rows, dtype=float)
                return pd.DataFrame(
                    {
                        "feature_a": x,
                        "feature_b": x % 3,
                        "future_return": np.where(x % 3 == 0, -0.01, np.where(x % 3 == 1, 0.0, 0.01)),
                        "target": (x % 3).astype(int),
                    }
                )

            make_split(0, 60).to_parquet(config.train_parquet)
            make_split(60, 20).to_parquet(config.val_parquet)
            make_split(80, 20).to_parquet(config.test_parquet)

            summary = run_baseline_models(
                data_config=config,
                apply_vif=False,
                random_seed=7,
                run_dir=run_dir,
            )

            self.assertIn("majority_class", summary["models"])
            self.assertIn("logistic_regression", summary["models"])
            self.assertIn("random_forest", summary["models"])
            self.assertTrue((run_dir / "baseline_results.json").exists())
