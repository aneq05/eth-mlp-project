import pickle
from pathlib import Path

import numpy as np
import optuna
import pandas as pd
import torch
from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score
from torch import nn
from torch.utils.data import DataLoader

from ..core.config import DataConfig, OptunaConfig, TrainingConfig
from ..core.utils import ensure_dir, save_json, set_seed
from ..data.dataset import TabularDataset
from ..evaluation.metrics import compute_classification_metrics
from ..evaluation.statistical_tests import bootstrap_metric_difference
from ..features.scaling import get_scaler
from ..modeling.ensemble import mean_probability_ensemble, prediction_uncertainty
from ..modeling.fit import fit_model
from ..modeling.inference import predict_classes, predict_probabilities
from ..modeling.losses import compute_class_weights
from ..modeling.network import MLPClassifier
from ..modeling.trial_selection import select_top_completed_trials


def _extract_feature_columns(df: pd.DataFrame) -> list[str]:
    return [c for c in df.columns if c not in {"target", "future_return"}]


def _build_optimizer(name: str, model: nn.Module, lr: float, weight_decay: float):
    name = name.lower()
    if name == "adam":
        return torch.optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    if name == "adamw":
        return torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=weight_decay)
    raise ValueError(f"Unsupported optimizer: {name}")


def _normalize_trial_params(params: dict) -> dict:
    n_layers = int(params["n_layers"])
    hidden_dims = [int(params[f"hidden_dim_{i+1}"]) for i in range(n_layers)]
    return {
        "hidden_dims": hidden_dims,
        "dropout": float(params["dropout"]),
        "activation": params["activation"],
        "use_batchnorm": bool(params["use_batchnorm"]),
        "lr": float(params["lr"]),
        "batch_size": int(params["batch_size"]),
        "weight_decay": float(params["weight_decay"]),
        "scaler_type": params["scaler_type"],
        "optimizer": params["optimizer"],
        "clip_grad_norm": float(params["clip_grad_norm"]),
    }


def run_top3_training_and_ensemble(
    data_config: DataConfig,
    optuna_config: OptunaConfig,
    training_config: TrainingConfig,
    random_seed: int = 42,
    validation_gap: int = 0,
) -> dict:
    set_seed(random_seed)

    train_df = pd.read_parquet(data_config.train_parquet)
    val_df = pd.read_parquet(data_config.val_parquet)
    test_df = pd.read_parquet(data_config.test_parquet)

    train_val_df = pd.concat([train_df, val_df], axis=0)
    feature_cols = _extract_feature_columns(train_val_df)

    # Internal chronological split for final training + early stopping.
    if validation_gap < 0:
        raise ValueError("validation_gap must be non-negative")
    split_idx = int(0.9 * len(train_val_df))
    val_start = split_idx + validation_gap
    final_train_df = train_val_df.iloc[:split_idx].copy()
    final_val_df = train_val_df.iloc[val_start:].copy()
    if final_train_df.empty or final_val_df.empty:
        raise ValueError("final train and validation splits must be non-empty after applying validation_gap")

    x_train = final_train_df[feature_cols].to_numpy(dtype=np.float32)
    y_train = final_train_df["target"].to_numpy(dtype=np.int64)
    x_val = final_val_df[feature_cols].to_numpy(dtype=np.float32)
    y_val = final_val_df["target"].to_numpy(dtype=np.int64)
    x_test = test_df[feature_cols].to_numpy(dtype=np.float32)
    y_test = test_df["target"].to_numpy(dtype=np.int64)

    study = optuna.load_study(study_name=optuna_config.study_name, storage=optuna_config.storage_url)
    sorted_trials = select_top_completed_trials(study.trials, limit=3, direction=optuna_config.direction)
    if len(sorted_trials) < 3:
        raise ValueError("Optuna has fewer than 3 completed trials. Run optuna search first.")

    device = torch.device(training_config.device)
    project_root = data_config.features_parquet.parents[2]
    checkpoints_dir = ensure_dir(project_root / "checkpoints" / "top3")
    tensorboard_dir = ensure_dir(project_root / "logs" / "tensorboard" / "final")
    predictions_dir = ensure_dir(project_root / "reports" / "predictions")

    all_probabilities: list[np.ndarray] = []
    model_results: list[dict] = []

    for rank, trial in enumerate(sorted_trials, start=1):
        params = _normalize_trial_params(trial.params)
        scaler = get_scaler(params["scaler_type"])
        x_train_scaled = scaler.fit_transform(x_train)
        x_val_scaled = scaler.transform(x_val)
        x_test_scaled = scaler.transform(x_test)

        train_loader = DataLoader(
            TabularDataset(x_train_scaled, y_train),
            batch_size=params["batch_size"],
            shuffle=True,
            num_workers=training_config.num_workers,
        )
        val_loader = DataLoader(
            TabularDataset(x_val_scaled, y_val),
            batch_size=params["batch_size"],
            shuffle=False,
            num_workers=training_config.num_workers,
        )
        test_loader = DataLoader(
            TabularDataset(x_test_scaled, y_test),
            batch_size=params["batch_size"],
            shuffle=False,
            num_workers=training_config.num_workers,
        )

        model = MLPClassifier(
            input_dim=len(feature_cols),
            hidden_dims=params["hidden_dims"],
            num_classes=3,
            activation=params["activation"],
            dropout=params["dropout"],
            use_batchnorm=params["use_batchnorm"],
        ).to(device)

        class_weights = compute_class_weights(y_train, num_classes=3).to(device)
        criterion = nn.CrossEntropyLoss(weight=class_weights)
        optimizer = _build_optimizer(
            name=params["optimizer"],
            model=model,
            lr=params["lr"],
            weight_decay=params["weight_decay"],
        )

        checkpoint_path = checkpoints_dir / f"model_rank_{rank}.pt"
        fit_model(
            model=model,
            train_loader=train_loader,
            val_loader=val_loader,
            criterion=criterion,
            optimizer=optimizer,
            device=device,
            epochs=training_config.epochs,
            checkpoint_path=checkpoint_path,
            tensorboard_log_dir=tensorboard_dir / f"model_rank_{rank}",
            monitor_metric=training_config.monitor_metric,
            monitor_mode=training_config.monitor_mode,
            early_stopping_patience=training_config.early_stopping_patience,
            clip_grad_norm=params["clip_grad_norm"],
        )

        checkpoint = torch.load(checkpoint_path, map_location=device)
        model.load_state_dict(checkpoint["model_state_dict"])
        probs = predict_probabilities(model=model, dataloader=test_loader, device=device)
        preds = predict_classes(probs)
        metrics = compute_classification_metrics(y_true=y_test, y_pred=preds)

        all_probabilities.append(probs)

        pred_df = pd.DataFrame(
            {
                "timestamp": test_df.index.astype(str),
                "y_true": y_test,
                "y_pred": preds,
                "prob_sell": probs[:, 0],
                "prob_hold": probs[:, 1],
                "prob_buy": probs[:, 2],
            }
        )
        pred_df.to_csv(predictions_dir / f"model_rank_{rank}_predictions.csv", index=False)

        with (checkpoints_dir / f"model_rank_{rank}_scaler.pkl").open("wb") as f:
            pickle.dump(scaler, f)
        save_json(
            {"trial_number": trial.number, "trial_value": float(trial.value), "params": params},
            checkpoints_dir / f"model_rank_{rank}_config.json",
        )

        model_results.append(
            {
                "rank": rank,
                "trial_number": trial.number,
                "cv_score": float(trial.value),
                "test_metrics": metrics,
            }
        )

    ensemble_probs, ensemble_preds = mean_probability_ensemble(all_probabilities)
    ensemble_metrics = compute_classification_metrics(y_true=y_test, y_pred=ensemble_preds)
    uncertainty = prediction_uncertainty(ensemble_probs)

    cv_best_single = model_results[0]
    cv_best_pred_path = predictions_dir / f"model_rank_{cv_best_single['rank']}_predictions.csv"
    cv_best_preds = pd.read_csv(cv_best_pred_path)["y_pred"].to_numpy(dtype=np.int64)

    bootstrap = {
        "f1_macro": bootstrap_metric_difference(
            y_true=y_test,
            y_pred_a=ensemble_preds,
            y_pred_b=cv_best_preds,
            metric_fn=lambda yt, yp: float(f1_score(yt, yp, average="macro", zero_division=0)),
        ),
        "balanced_accuracy": bootstrap_metric_difference(
            y_true=y_test,
            y_pred_a=ensemble_preds,
            y_pred_b=cv_best_preds,
            metric_fn=lambda yt, yp: float(balanced_accuracy_score(yt, yp)),
        ),
        "accuracy": bootstrap_metric_difference(
            y_true=y_test,
            y_pred_a=ensemble_preds,
            y_pred_b=cv_best_preds,
            metric_fn=lambda yt, yp: float(accuracy_score(yt, yp)),
        ),
    }

    ensemble_df = pd.DataFrame(
        {
            "timestamp": test_df.index.astype(str),
            "y_true": y_test,
            "y_pred": ensemble_preds,
            "prob_sell": ensemble_probs[:, 0],
            "prob_hold": ensemble_probs[:, 1],
            "prob_buy": ensemble_probs[:, 2],
            "entropy": uncertainty["entropy"],
            "margin": uncertainty["margin"],
        }
    )
    ensemble_df.to_csv(predictions_dir / "ensemble_predictions.csv", index=False)

    summary = {
        "top3_models": model_results,
        "ensemble_metrics": ensemble_metrics,
        "cv_best_single_model": cv_best_single,
        "bootstrap_ensemble_vs_cv_best": bootstrap,
        "feature_count": len(feature_cols),
        "validation_gap": int(validation_gap),
    }
    save_json(summary, project_root / "reports" / "final_results_summary.json")
    return summary
