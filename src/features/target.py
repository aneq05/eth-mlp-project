import pandas as pd


def _get_timestamp_index(df: pd.DataFrame, timestamp_col: str) -> pd.DatetimeIndex:
    if isinstance(df.index, pd.DatetimeIndex):
        timestamps = pd.DatetimeIndex(df.index)
    elif timestamp_col in df.columns:
        timestamps = pd.DatetimeIndex(pd.to_datetime(df[timestamp_col], utc=True, errors="coerce"))
    else:
        raise ValueError("DataFrame must have a DatetimeIndex or a timestamp column")

    if timestamps.isna().any():
        raise ValueError("timestamps contain invalid or missing values")
    if timestamps.has_duplicates:
        raise ValueError("timestamps must be unique")
    return timestamps


def make_multiclass_target(
    df: pd.DataFrame,
    horizon: int = 6,
    threshold: float = 0.0075,
    close_col: str = "close",
    timestamp_col: str = "timestamp",
) -> pd.DataFrame:
    if horizon <= 0:
        raise ValueError("horizon must be a positive integer")
    if threshold < 0:
        raise ValueError("threshold must be non-negative")
    if close_col not in df.columns:
        raise ValueError(f"close_col '{close_col}' is not present in the dataframe")

    work = df.copy()
    timestamps = _get_timestamp_index(work, timestamp_col=timestamp_col)
    work = work.assign(_target_timestamp=timestamps).sort_values("_target_timestamp")

    timestamps = pd.DatetimeIndex(work["_target_timestamp"])
    close_by_timestamp = pd.Series(work[close_col].to_numpy(), index=timestamps)
    future_close = close_by_timestamp.reindex(timestamps + pd.Timedelta(hours=horizon)).to_numpy()
    future_return = pd.Series(future_close, index=work.index) / work[close_col] - 1.0

    work["future_return"] = future_return

    work["target"] = 1
    work.loc[future_return < -threshold, "target"] = 0
    work.loc[future_return > threshold, "target"] = 2

    work = work.dropna(subset=["future_return"]).drop(columns=["_target_timestamp"]).copy()
    work["target"] = work["target"].astype(int)
    return work
