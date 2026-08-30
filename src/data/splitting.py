from collections.abc import Iterator

import numpy as np
import pandas as pd


def chronological_train_val_test_split(
    df: pd.DataFrame,
    train_ratio: float = 0.70,
    val_ratio: float = 0.15,
    test_ratio: float = 0.15,
    gap: int = 0,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    if not np.isclose(train_ratio + val_ratio + test_ratio, 1.0):
        raise ValueError("train_ratio + val_ratio + test_ratio must equal 1.0")
    if gap < 0:
        raise ValueError("gap must be non-negative")

    n = len(df)
    train_end = int(n * train_ratio)
    val_start = train_end + gap
    val_end = val_start + int(n * val_ratio)
    test_start = val_end + gap

    train_df = df.iloc[:train_end].copy()
    val_df = df.iloc[val_start:val_end].copy()
    test_df = df.iloc[test_start:].copy()

    if train_df.empty or val_df.empty or test_df.empty:
        raise ValueError("train, validation, and test splits must be non-empty after applying gap")
    return train_df, val_df, test_df


def time_series_cv_indices(
    n_samples: int,
    n_splits: int = 5,
    gap: int = 0,
) -> Iterator[tuple[np.ndarray, np.ndarray]]:
    from sklearn.model_selection import TimeSeriesSplit

    splitter = TimeSeriesSplit(n_splits=n_splits, gap=gap)
    indices = np.arange(n_samples)
    yield from splitter.split(indices)
