import pandas as pd
from unittest import TestCase

from src.data.splitting import chronological_train_val_test_split


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

    def test_rejects_invalid_ratios(self) -> None:
        df = pd.DataFrame({"value": range(10)})

        with self.assertRaisesRegex(ValueError, "must equal 1.0"):
            chronological_train_val_test_split(df, train_ratio=0.5, val_ratio=0.2, test_ratio=0.2)
