import importlib.util
import unittest

import pandas as pd
from unittest import TestCase

from src.data.splitting import chronological_train_val_test_split, time_series_cv_indices


class TestChronologicalSplit(TestCase):
    def test_preserves_order(self) -> None:
        df = pd.DataFrame({"value": range(10)})

        train_df, val_df, test_df = chronological_train_val_test_split(
            df,
            train_ratio=0.6,
            val_ratio=0.2,
            test_ratio=0.2,
        )

        self.assertEqual(train_df["value"].tolist(), [0, 1, 2, 3, 4, 5])
        self.assertEqual(val_df["value"].tolist(), [6, 7])
        self.assertEqual(test_df["value"].tolist(), [8, 9])

    def test_applies_gap_between_splits(self) -> None:
        df = pd.DataFrame({"value": range(12)})

        train_df, val_df, test_df = chronological_train_val_test_split(
            df,
            train_ratio=0.5,
            val_ratio=0.25,
            test_ratio=0.25,
            gap=1,
        )

        self.assertEqual(train_df["value"].tolist(), [0, 1, 2, 3, 4, 5])
        self.assertEqual(val_df["value"].tolist(), [7, 8, 9])
        self.assertEqual(test_df["value"].tolist(), [11])

    def test_rejects_invalid_ratios(self) -> None:
        df = pd.DataFrame({"value": range(10)})

        with self.assertRaisesRegex(ValueError, "must equal 1.0"):
            chronological_train_val_test_split(df, train_ratio=0.5, val_ratio=0.2, test_ratio=0.2)

    @unittest.skipUnless(importlib.util.find_spec("sklearn") is not None, "scikit-learn is not installed")
    def test_time_series_cv_applies_gap_before_validation_fold(self) -> None:
        for train_idx, val_idx in time_series_cv_indices(n_samples=12, n_splits=3, gap=2):
            self.assertLess(train_idx[-1], val_idx[0])
            self.assertEqual(val_idx[0] - train_idx[-1] - 1, 2)
