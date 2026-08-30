import pandas as pd
from unittest import TestCase

from src.features.selection import drop_constant_features, drop_highly_correlated_features


class TestFeatureSelection(TestCase):
    def test_drop_constant_features_removes_single_value_columns(self) -> None:
        df = pd.DataFrame(
            {
                "constant": [1, 1, 1],
                "varying": [1, 2, 3],
            }
        )

        filtered, dropped = drop_constant_features(df)

        self.assertEqual(dropped, ["constant"])
        self.assertEqual(filtered.columns.tolist(), ["varying"])

    def test_drop_highly_correlated_features_removes_later_duplicate_signal(self) -> None:
        df = pd.DataFrame(
            {
                "base": [1, 2, 3, 4],
                "duplicate": [2, 4, 6, 8],
                "other": [4, 1, 3, 2],
            }
        )

        filtered, dropped = drop_highly_correlated_features(df, threshold=0.99)

        self.assertEqual(dropped, ["duplicate"])
        self.assertEqual(filtered.columns.tolist(), ["base", "other"])
