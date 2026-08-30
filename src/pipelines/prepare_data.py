from pathlib import Path

import numpy as np
import pandas as pd

from ..core.config import DataConfig, SplitConfig, TargetConfig
from ..core.utils import ensure_dir, save_json
from ..data.cleaning import clean_ohlcv
from ..data.load import load_ohlcv_csv, save_dataframe
from ..data.splitting import chronological_train_val_test_split
from ..features.engineering import create_features
from ..features.selection import (
    drop_constant_features,
    drop_highly_correlated_features,
    reduce_vif_features,
)
from ..features.target import make_multiclass_target


def prepare_datasets(
    data_config: DataConfig,
    target_config: TargetConfig,
    split_config: SplitConfig,
    corr_threshold: float = 0.95,
    apply_vif: bool = True,
    vif_threshold: float = 10.0,
) -> dict:
    raw_df = load_ohlcv_csv(data_config.raw_csv)
    clean_df, cleaning_stats = clean_ohlcv(raw_df)
    save_dataframe(clean_df, data_config.clean_csv)

    feat_df = create_features(clean_df)
    feat_df = make_multiclass_target(
        feat_df,
        horizon=target_config.horizon,
        threshold=target_config.threshold,
    )
    feat_df = feat_df.replace([np.inf, -np.inf], np.nan).dropna().copy()

    train_full, val_full, test_full = chronological_train_val_test_split(
        feat_df,
        train_ratio=split_config.train_ratio,
        val_ratio=split_config.val_ratio,
        test_ratio=split_config.test_ratio,
        gap=target_config.horizon,
    )

    protected_cols = {"target", "future_return"}
    train_features = train_full.drop(columns=list(protected_cols)).select_dtypes(include=["number"]).copy()
    train_features, dropped_constant = drop_constant_features(train_features)
    train_features, dropped_corr = drop_highly_correlated_features(train_features, threshold=corr_threshold)

    dropped_vif: list[str] = []
    if apply_vif:
        train_features, dropped_vif = reduce_vif_features(train_features, vif_threshold=vif_threshold)

    feature_columns = list(train_features.columns)

    def _apply_selected_features(split_df: pd.DataFrame) -> pd.DataFrame:
        selected = split_df.loc[:, feature_columns].copy()
        selected["future_return"] = split_df["future_return"].astype(float)
        selected["target"] = split_df["target"].astype(int)
        return selected.replace([np.inf, -np.inf], np.nan).dropna().copy()

    train_df = _apply_selected_features(train_full)
    val_df = _apply_selected_features(val_full)
    test_df = _apply_selected_features(test_full)
    final_df = pd.concat([train_df, val_df, test_df], axis=0)

    save_dataframe(final_df, data_config.features_parquet)
    save_dataframe(train_df, data_config.train_parquet)
    save_dataframe(val_df, data_config.val_parquet)
    save_dataframe(test_df, data_config.test_parquet)

    reports_dir = data_config.features_parquet.parents[2] / "reports"
    ensure_dir(reports_dir)

    class_counts = final_df["target"].value_counts().sort_index().to_dict()
    metadata = {
        "cleaning_stats": cleaning_stats,
        "rows_final_dataset": len(final_df),
        "split_sizes": {"train": len(train_df), "val": len(val_df), "test": len(test_df)},
        "class_counts": {str(k): int(v) for k, v in class_counts.items()},
        "split_gap_rows": int(target_config.horizon),
        "num_features": int(len(feature_columns)),
        "feature_columns": feature_columns,
        "dropped_features": {
            "constant": dropped_constant,
            "high_corr": dropped_corr,
            "high_vif": dropped_vif,
        },
        "target_config": {
            "horizon": target_config.horizon,
            "horizon_unit": "hours",
            "threshold": target_config.threshold,
        },
    }
    save_json(metadata, reports_dir / "data_prep_metadata.json")
    return metadata


def load_processed_splits(data_config: DataConfig) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    train_df = pd.read_parquet(data_config.train_parquet)
    val_df = pd.read_parquet(data_config.val_parquet)
    test_df = pd.read_parquet(data_config.test_parquet)
    return train_df, val_df, test_df
