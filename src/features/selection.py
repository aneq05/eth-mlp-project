import numpy as np
import pandas as pd


def fit_feature_selection(
    train_df: pd.DataFrame,
    protected_cols: set[str] | None = None,
    corr_threshold: float = 0.95,
    apply_vif: bool = True,
    vif_threshold: float = 10.0,
) -> tuple[list[str], dict[str, list[str]]]:
    protected_cols = {"target", "future_return"} if protected_cols is None else protected_cols
    train_features = train_df.drop(columns=list(protected_cols), errors="ignore").select_dtypes(include=["number"])
    train_features = train_features.replace([np.inf, -np.inf], np.nan).dropna().copy()

    selected, dropped_constant = drop_constant_features(train_features)
    selected, dropped_corr = drop_highly_correlated_features(selected, threshold=corr_threshold)

    dropped_vif: list[str] = []
    if apply_vif:
        selected, dropped_vif = reduce_vif_features(selected, vif_threshold=vif_threshold)

    return list(selected.columns), {
        "constant": dropped_constant,
        "high_corr": dropped_corr,
        "high_vif": dropped_vif,
    }


def apply_feature_selection(split_df: pd.DataFrame, feature_columns: list[str]) -> pd.DataFrame:
    selected = split_df.loc[:, feature_columns].copy()
    selected["future_return"] = split_df["future_return"].astype(float)
    selected["target"] = split_df["target"].astype(int)
    return selected.replace([np.inf, -np.inf], np.nan).dropna().copy()


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
    from statsmodels.stats.outliers_influence import variance_inflation_factor

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
