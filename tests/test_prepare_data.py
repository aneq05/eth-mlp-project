import tempfile
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

import numpy as np
import pandas as pd

from src.core.config import DataConfig, SplitConfig, TargetConfig
from src.pipelines.prepare_data import prepare_datasets


class TestPrepareDatasets(TestCase):
    def test_prepare_data_preserves_unselected_features_and_removes_inf(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            raw_csv = root / "raw.csv"
            close = np.linspace(100, 130, 16)
            pd.DataFrame(
                {
                    "timestamp": pd.date_range("2026-01-01", periods=16, freq="h", tz="UTC"),
                    "open": close,
                    "high": close + 1,
                    "low": close - 1,
                    "close": close,
                    "volume": np.ones(16),
                }
            ).to_csv(raw_csv, index=False)

            def fake_create_features(df: pd.DataFrame) -> pd.DataFrame:
                out = df.copy()
                out["stable_signal"] = np.arange(len(out), dtype=float)
                out["late_only_signal"] = [1.0] * 9 + list(np.arange(7, dtype=float))
                out.iloc[2, out.columns.get_loc("stable_signal")] = np.inf
                return out

            data_config = DataConfig(
                raw_csv=raw_csv,
                clean_csv=root / "data" / "clean" / "clean.csv",
                features_parquet=root / "data" / "processed" / "features.csv",
                train_parquet=root / "data" / "processed" / "train.csv",
                val_parquet=root / "data" / "processed" / "val.csv",
                test_parquet=root / "data" / "processed" / "test.csv",
            )

            with patch("src.pipelines.prepare_data.create_features", side_effect=fake_create_features):
                metadata = prepare_datasets(
                    data_config=data_config,
                    target_config=TargetConfig(horizon=1, threshold=0.01),
                    split_config=SplitConfig(train_ratio=0.5, val_ratio=0.25, test_ratio=0.25),
                )

            train_df = pd.read_csv(data_config.train_parquet)
            val_df = pd.read_csv(data_config.val_parquet)
            test_df = pd.read_csv(data_config.test_parquet)

            self.assertEqual(metadata["feature_selection"], "deferred_to_cv_and_final_training")
            self.assertIn("late_only_signal", train_df.columns)
            self.assertIn("late_only_signal", val_df.columns)
            self.assertIn("late_only_signal", test_df.columns)
            self.assertFalse(np.isinf(train_df.select_dtypes(include=["number"]).to_numpy()).any())
            self.assertEqual(metadata["split_gap_rows"], 1)
