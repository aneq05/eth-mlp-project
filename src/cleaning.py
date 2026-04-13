import pandas as pd


def clean_ohlcv(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, int]]:
    stats: dict[str, int] = {}

    work = df.copy()
    stats["rows_initial"] = len(work)

    work["timestamp"] = pd.to_datetime(work["timestamp"], utc=True, errors="coerce")
    work = work.dropna(subset=["timestamp"]).sort_values("timestamp")
    work = work.set_index("timestamp")

    duplicated_ts = int(work.index.duplicated().sum())
    stats["duplicated_timestamps"] = duplicated_ts
    work = work[~work.index.duplicated(keep="first")]

    numeric_cols = ["open", "high", "low", "close", "volume"]
    for col in numeric_cols:
        work[col] = pd.to_numeric(work[col], errors="coerce")

    nan_before = int(work[numeric_cols].isna().sum().sum())
    stats["nan_before_drop"] = nan_before
    work = work.dropna(subset=numeric_cols)

    invalid_candles = (
        (work["high"] < work[["open", "close"]].max(axis=1))
        | (work["low"] > work[["open", "close"]].min(axis=1))
        | (work["volume"] < 0)
    )
    stats["invalid_candles"] = int(invalid_candles.sum())
    work = work[~invalid_candles]

    stats["rows_final"] = len(work)
    return work, stats
