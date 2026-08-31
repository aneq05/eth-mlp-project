from pathlib import Path
from unittest import TestCase

from src.core.config import DataConfig


class TestDataConfig(TestCase):
    def test_with_run_dir_moves_processed_outputs_under_run_data_dir(self) -> None:
        run_dir = Path("reports") / "runs" / "example"
        config = DataConfig(raw_csv=Path("data") / "raw" / "eth.csv").with_run_dir(run_dir)

        self.assertEqual(config.raw_csv, Path("data") / "raw" / "eth.csv")
        self.assertEqual(config.clean_csv, run_dir / "data" / "clean.csv")
        self.assertEqual(config.features_parquet, run_dir / "data" / "features.parquet")
        self.assertEqual(config.train_parquet, run_dir / "data" / "train.parquet")
        self.assertEqual(config.val_parquet, run_dir / "data" / "val.parquet")
        self.assertEqual(config.test_parquet, run_dir / "data" / "test.parquet")
