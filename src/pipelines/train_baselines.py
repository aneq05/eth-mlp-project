from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from ..core.config import DataConfig
from ..core.utils import ensure_dir, save_json
from ..evaluation.metrics import compute_classification_metrics
from ..features.selection import apply_feature_selection, fit_feature_selection


def _majority_predictions(y_train: np.ndarray, n_test: int) -> np.ndarray:
    labels, counts = np.unique(y_train, return_counts=True)
    majority_label = labels[int(np.argmax(counts))]
    return np.full(n_test, majority_label, dtype=np.int64)


def run_baseline_models(
    data_config: DataConfig,
    corr_threshold: float = 0.95,
    apply_vif: bool = False,
    vif_threshold: float = 10.0,
    random_seed: int = 42,
    run_dir: str | Path | None = None,
) -> dict:
    train_df = pd.read_parquet(data_config.train_parquet)
    val_df = pd.read_parquet(data_config.val_parquet)
    test_df = pd.read_parquet(data_config.test_parquet)
    train_val_df = pd.concat([train_df, val_df], axis=0)

    feature_cols, feature_selection_report = fit_feature_selection(
        train_val_df,
        corr_threshold=corr_threshold,
        apply_vif=apply_vif,
        vif_threshold=vif_threshold,
    )
    train_val_selected = apply_feature_selection(train_val_df, feature_cols)
    test_selected = apply_feature_selection(test_df, feature_cols)

    x_train = train_val_selected[feature_cols].to_numpy(dtype=np.float32)
    y_train = train_val_selected["target"].to_numpy(dtype=np.int64)
    x_test = test_selected[feature_cols].to_numpy(dtype=np.float32)
    y_test = test_selected["target"].to_numpy(dtype=np.int64)

    models = {
        "majority_class": None,
        "logistic_regression": Pipeline(
            [
                ("scaler", StandardScaler()),
                (
                    "model",
                    LogisticRegression(
                        class_weight="balanced",
                        max_iter=1000,
                        random_state=random_seed,
                    ),
                ),
            ]
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=200,
            max_depth=8,
            class_weight="balanced_subsample",
            n_jobs=-1,
            random_state=random_seed,
        ),
    }

    results: dict[str, dict] = {}
    for model_name, model in models.items():
        if model is None:
            preds = _majority_predictions(y_train, n_test=len(y_test))
        else:
            model.fit(x_train, y_train)
            preds = model.predict(x_test)
        results[model_name] = compute_classification_metrics(y_true=y_test, y_pred=preds)

    output = {
        "models": results,
        "feature_count": len(feature_cols),
        "feature_columns": feature_cols,
        "feature_selection": feature_selection_report,
        "feature_selection_scope": "train_plus_validation_only",
        "random_seed": random_seed,
    }

    if run_dir is not None:
        output_dir = ensure_dir(run_dir)
        save_json(output, output_dir / "baseline_results.json")
    return output
