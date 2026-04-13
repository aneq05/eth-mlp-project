import numpy as np
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor


def drop_constant_features(df: pd.DataFrame, min_unique: int = 2) -> tuple[pd.DataFrame, list[str]]:
    to_drop = [col for col in df.columns if df[col].nunique(dropna=False) < min_unique]
    return df.drop(columns=to_drop), to_drop


def drop_highly_correlated_features(
    df: pd.DataFrame,
    threshold: float = 0.95,
) -> tuple[pd.DataFrame, list[str]]:
    corr = df.corr(numeric_only=True).abs()
    upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    to_drop = [column for column in upper.columns if any(upper[column] > threshold)]
    return df.drop(columns=to_drop), to_drop


def reduce_vif_features(
    df: pd.DataFrame,
    vif_threshold: float = 10.0,
    max_iter: int = 50,
) -> tuple[pd.DataFrame, list[str]]:
    work = df.copy()
    dropped: list[str] = []

    numeric_cols = list(work.select_dtypes(include=[np.number]).columns)
    work = work[numeric_cols]
    work = work.replace([np.inf, -np.inf], np.nan).dropna()

    if work.empty or work.shape[1] < 2:
        return df, dropped

    for _ in range(max_iter):
        vif_values = []
        for i in range(work.shape[1]):
            vif = variance_inflation_factor(work.values, i)
            vif_values.append(vif)

        max_vif = float(np.max(vif_values))
        if max_vif <= vif_threshold:
            break

        idx = int(np.argmax(vif_values))
        col_to_drop = work.columns[idx]
        dropped.append(col_to_drop)
        work = work.drop(columns=[col_to_drop])

        if work.shape[1] < 2:
            break

    kept_cols = [c for c in df.columns if c not in dropped]
    return df[kept_cols].copy(), dropped
