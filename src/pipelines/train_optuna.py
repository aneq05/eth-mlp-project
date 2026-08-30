from pathlib import Path

import numpy as np
import optuna
import pandas as pd
import torch
from torch import nn
from torch.utils.data import DataLoader

from ..core.config import DataConfig, OptunaConfig, TrainingConfig
from ..core.utils import ensure_dir, save_json, set_seed
from ..data.dataset import TabularDataset
from ..data.splitting import time_series_cv_indices
from ..modeling.losses import compute_class_weights
from ..modeling.network import MLPClassifier
from ..modeling.optuna_search import create_study, suggest_mlp_params
from ..modeling.train import train_one_epoch
from ..modeling.trial_selection import select_top_completed_trials
from ..modeling.validate import validate_one_epoch
from ..features.scaling import get_scaler


def _extract_feature_columns(df: pd.DataFrame) -> list[str]:
    return [c for c in df.columns if c not in {"target", "future_return"}]


def _build_optimizer(name: str, model: nn.Module, lr: float, weight_decay: float):
    name = name.lower()
    if name == "adam":
        return torch.optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    if name == "adamw":
        return torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=weight_decay)
    raise ValueError(f"Unsupported optimizer: {name}")


def _train_fold(
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_val: np.ndarray,
    y_val: np.ndarray,
    params: dict,
    training_config: TrainingConfig,
    device: torch.device,
) -> float:
    scaler = get_scaler(params["scaler_type"])
    x_train_scaled = scaler.fit_transform(x_train)
    x_val_scaled = scaler.transform(x_val)

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

    model = MLPClassifier(
        input_dim=x_train.shape[1],
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

    best_f1 = -np.inf
    bad_epochs = 0
    for _ in range(training_config.epochs):
        train_one_epoch(
            model=model,
            dataloader=train_loader,
            criterion=criterion,
            optimizer=optimizer,
            device=device,
            clip_grad_norm=params["clip_grad_norm"],
        )
        val_metrics = validate_one_epoch(model=model, dataloader=val_loader, criterion=criterion, device=device)
        current_f1 = val_metrics["f1_macro"]
        if current_f1 > best_f1:
            best_f1 = current_f1
            bad_epochs = 0
        else:
            bad_epochs += 1
            if bad_epochs >= training_config.early_stopping_patience:
                break
    return float(best_f1)


def run_optuna_time_series_search(
    data_config: DataConfig,
    optuna_config: OptunaConfig,
    training_config: TrainingConfig,
    n_splits: int = 5,
    cv_gap: int = 0,
    random_seed: int | None = None,
) -> dict:
    seed = optuna_config.seed if random_seed is None else random_seed
    if seed is not None:
        set_seed(seed)

    train_df = pd.read_parquet(data_config.train_parquet)
    val_df = pd.read_parquet(data_config.val_parquet)
    train_val_df = pd.concat([train_df, val_df], axis=0)

    feature_cols = _extract_feature_columns(train_val_df)
    x_all = train_val_df[feature_cols].to_numpy(dtype=np.float32)
    y_all = train_val_df["target"].to_numpy(dtype=np.int64)

    device = torch.device(training_config.device)

    def objective(trial: optuna.Trial) -> float:
        params = suggest_mlp_params(trial)
        fold_scores: list[float] = []

        for train_idx, val_idx in time_series_cv_indices(len(train_val_df), n_splits=n_splits, gap=cv_gap):
            x_train, y_train = x_all[train_idx], y_all[train_idx]
            x_val, y_val = x_all[val_idx], y_all[val_idx]

            score = _train_fold(
                x_train=x_train,
                y_train=y_train,
                x_val=x_val,
                y_val=y_val,
                params=params,
                training_config=training_config,
                device=device,
            )
            fold_scores.append(score)
            trial.report(np.mean(fold_scores), step=len(fold_scores))
            if trial.should_prune():
                raise optuna.TrialPruned()

        return float(np.mean(fold_scores))

    study = create_study(
        study_name=optuna_config.study_name,
        storage_url=optuna_config.storage_url,
        direction=optuna_config.direction,
        reset_study=optuna_config.reset_study,
        sampler_seed=seed,
    )
    study.optimize(objective, n_trials=optuna_config.n_trials, timeout=optuna_config.timeout_seconds)

    reports_dir = Path(data_config.features_parquet).parents[2] / "reports"
    ensure_dir(reports_dir)
    top_trials = []
    selected_trials = select_top_completed_trials(study.trials, limit=5, direction=optuna_config.direction)
    if not selected_trials:
        raise ValueError("Optuna search finished without completed trials.")

    for trial in selected_trials:
        top_trials.append(
            {
                "number": trial.number,
                "value": float(trial.value),
                "params": trial.params,
            }
        )

    payload = {
        "study_name": optuna_config.study_name,
        "best_value": float(selected_trials[0].value),
        "best_trial_number": int(selected_trials[0].number),
        "best_params": selected_trials[0].params,
        "top_trials": top_trials,
        "feature_count": len(feature_cols),
        "n_splits": n_splits,
        "cv_gap": int(cv_gap),
        "seed": seed,
        "reset_study": optuna_config.reset_study,
    }
    save_json(payload, reports_dir / "optuna_summary.json")
    return payload
