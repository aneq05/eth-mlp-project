from collections.abc import Callable

import optuna

from .trial_selection import select_top_completed_trials


def suggest_mlp_params(trial: optuna.Trial) -> dict:
    n_layers = trial.suggest_int("n_layers", 2, 5)
    hidden_dims = []
    for i in range(n_layers):
        hidden_dims.append(trial.suggest_int(f"hidden_dim_{i+1}", 32, 512, step=32))

    params = {
        "n_layers": n_layers,
        "hidden_dims": hidden_dims,
        "dropout": trial.suggest_float("dropout", 0.0, 0.5),
        "activation": trial.suggest_categorical("activation", ["relu", "leaky_relu", "gelu"]),
        "use_batchnorm": trial.suggest_categorical("use_batchnorm", [True, False]),
        "lr": trial.suggest_float("lr", 1e-5, 1e-2, log=True),
        "batch_size": trial.suggest_categorical("batch_size", [32, 64, 128, 256]),
        "weight_decay": trial.suggest_float("weight_decay", 1e-7, 1e-3, log=True),
        "scaler_type": trial.suggest_categorical("scaler_type", ["standard", "robust"]),
        "optimizer": trial.suggest_categorical("optimizer", ["adam", "adamw"]),
        "clip_grad_norm": trial.suggest_float("clip_grad_norm", 0.5, 5.0),
    }
    return params


def create_study(
    study_name: str,
    storage_url: str,
    direction: str = "maximize",
    load_if_exists: bool = True,
    reset_study: bool = False,
    sampler_seed: int | None = None,
) -> optuna.Study:
    if reset_study:
        try:
            optuna.delete_study(study_name=study_name, storage=storage_url)
        except KeyError:
            pass

    sampler = optuna.samplers.TPESampler(seed=sampler_seed) if sampler_seed is not None else None
    return optuna.create_study(
        study_name=study_name,
        storage=storage_url,
        direction=direction,
        load_if_exists=load_if_exists,
        sampler=sampler,
    )


def run_optuna_search(
    objective_fn: Callable[[optuna.Trial], float],
    study_name: str,
    storage_url: str,
    direction: str = "maximize",
    n_trials: int = 30,
    timeout_seconds: int | None = None,
    reset_study: bool = False,
    sampler_seed: int | None = None,
) -> optuna.Study:
    study = create_study(
        study_name=study_name,
        storage_url=storage_url,
        direction=direction,
        reset_study=reset_study,
        sampler_seed=sampler_seed,
    )
    study.optimize(objective_fn, n_trials=n_trials, timeout=timeout_seconds)
    return study


__all__ = [
    "create_study",
    "run_optuna_search",
    "select_top_completed_trials",
    "suggest_mlp_params",
]
