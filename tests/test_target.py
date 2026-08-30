import pandas as pd
from unittest import TestCase

from src.features.target import make_multiclass_target


class TestMakeMulticlassTarget(TestCase):
    def test_assigns_sell_hold_buy_labels(self) -> None:
        df = pd.DataFrame(
            {
                "timestamp": pd.date_range("2026-01-01", periods=4, freq="h", tz="UTC"),
                "close": [100.0, 98.0, 100.0, 103.0],
            }
        )

        result = make_multiclass_target(df, horizon=1, threshold=0.01)

        self.assertEqual(result["target"].tolist(), [0, 2, 2])
        self.assertEqual(result["future_return"].round(4).tolist(), [-0.0200, 0.0204, 0.0300])

    def test_uses_timestamp_horizon_instead_of_row_offset(self) -> None:
        df = pd.DataFrame(
            {
                "timestamp": pd.to_datetime(
                    ["2026-01-01 00:00", "2026-01-01 01:00", "2026-01-01 03:00"],
                    utc=True,
                ),
                "close": [100.0, 110.0, 130.0],
            }
        )

        result = make_multiclass_target(df, horizon=1, threshold=0.01)

        self.assertEqual(result["timestamp"].astype(str).tolist(), ["2026-01-01 00:00:00+00:00"])
        self.assertEqual(result["future_return"].round(4).tolist(), [0.1000])

    def test_rejects_invalid_horizon(self) -> None:
        df = pd.DataFrame(
            {
                "timestamp": pd.date_range("2026-01-01", periods=2, freq="h", tz="UTC"),
                "close": [100.0, 101.0],
            }
        )

        with self.assertRaisesRegex(ValueError, "horizon"):
            make_multiclass_target(df, horizon=0)

    def test_rejects_missing_close_column(self) -> None:
        df = pd.DataFrame(
            {
                "timestamp": pd.date_range("2026-01-01", periods=2, freq="h", tz="UTC"),
                "price": [100.0, 101.0],
            }
        )

        with self.assertRaisesRegex(ValueError, "close_col"):
            make_multiclass_target(df)

    def test_rejects_missing_timestamp_information(self) -> None:
        df = pd.DataFrame({"close": [100.0, 101.0]})

        with self.assertRaisesRegex(ValueError, "DatetimeIndex or a timestamp column"):
            make_multiclass_target(df)
