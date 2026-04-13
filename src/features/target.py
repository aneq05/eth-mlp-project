import pandas as pd


def make_multiclass_target(
    df: pd.DataFrame,
    horizon: int = 6,
    threshold: float = 0.0075,
    close_col: str = "close",
) -> pd.DataFrame:
    work = df.copy()
    future_return = work[close_col].shift(-horizon) / work[close_col] - 1.0
    work["future_return"] = future_return

    work["target"] = 1
    work.loc[future_return < -threshold, "target"] = 0
    work.loc[future_return > threshold, "target"] = 2

    # Last horizon rows do not have valid target.
    work = work.iloc[:-horizon].copy()
    return work
