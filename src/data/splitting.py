from collections.abc import Iterator

import numpy as np
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit


def chronological_train_val_test_split(
    df: pd.DataFrame,
    train_ratio: float = 0.70,
    val_ratio: float = 0.15,
    test_ratio: float = 0.15,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    if not np.isclose(train_ratio + val_ratio + test_ratio, 1.0):
        raise ValueError("train_ratio + val_ratio + test_ratio must equal 1.0")

    n = len(df)
    train_end = int(n * train_ratio)
    val_end = train_end + int(n * val_ratio)

    train_df = df.iloc[:train_end].copy()
    val_df = df.iloc[train_end:val_end].copy()
    test_df = df.iloc[val_end:].copy()
    return train_df, val_df, test_df


def time_series_cv_indices(
    n_samples: int,
    n_splits: int = 5,
) -> Iterator[tuple[np.ndarray, np.ndarray]]:
    splitter = TimeSeriesSplit(n_splits=n_splits)
    indices = np.arange(n_samples)
    for train_idx, val_idx in splitter.split(indices):
        yield train_idx, val_idx
