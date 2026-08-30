import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.core.config import DataConfig, OptunaConfig, TrainingConfig
from src.pipelines.train_optuna import run_optuna_time_series_search


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Optuna time-series cross-validation search.")
    parser.add_argument("--n-trials", type=int, default=30, help="Number of Optuna trials.")
    parser.add_argument("--epochs", type=int, default=20, help="Epochs per fold in each trial.")
    parser.add_argument("--patience", type=int, default=5, help="Early stopping patience.")
    parser.add_argument("--n-splits", type=int, default=5, help="Number of time-series CV splits.")
    parser.add_argument("--cv-gap", type=int, default=6, help="Purged gap between CV train and validation folds.")
    parser.add_argument("--study-name", type=str, default="eth_mlp_optimization", help="Optuna study name.")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for training and Optuna sampler.")
    parser.add_argument(
        "--reset-study",
        action="store_true",
        help="Delete an existing study with the same name before running new trials.",
    )
    parser.add_argument("--device", type=str, default="cpu", help="Device, e.g. cpu or cuda.")
    args = parser.parse_args()

    training_config = TrainingConfig(
        epochs=args.epochs,
        early_stopping_patience=args.patience,
        device=args.device,
    )
    optuna_config = OptunaConfig(
        study_name=args.study_name,
        n_trials=args.n_trials,
        seed=args.seed,
        reset_study=args.reset_study,
    )

    summary = run_optuna_time_series_search(
        data_config=DataConfig(),
        optuna_config=optuna_config,
        training_config=training_config,
        n_splits=args.n_splits,
        cv_gap=args.cv_gap,
    )
    print("Optuna search completed.")
    print(summary)


if __name__ == "__main__":
    main()
