import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.core.config import DataConfig, OptunaConfig, SplitConfig, TargetConfig, TrainingConfig
from src.pipelines.evaluate_models import evaluate_saved_predictions
from src.pipelines.prepare_data import prepare_datasets
from src.pipelines.train_optuna import run_optuna_time_series_search
from src.pipelines.train_top3 import run_top3_training_and_ensemble


def main() -> None:
    parser = argparse.ArgumentParser(description="Run full ETH MLP pipeline end-to-end.")
    parser.add_argument("--raw-csv", type=str, default=None, help="Path to raw ETHUSDT 1h CSV.")
    parser.add_argument("--horizon", type=int, default=6)
    parser.add_argument("--threshold", type=float, default=0.0075)
    parser.add_argument("--n-trials", type=int, default=30)
    parser.add_argument("--optuna-epochs", type=int, default=20)
    parser.add_argument("--final-epochs", type=int, default=50)
    parser.add_argument("--study-name", type=str, default="eth_mlp_optimization")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--reset-study", action="store_true")
    parser.add_argument("--device", type=str, default="cpu")
    args = parser.parse_args()

    data_config = DataConfig()
    if args.raw_csv:
        data_config.raw_csv = args.raw_csv

    prepare_datasets(
        data_config=data_config,
        target_config=TargetConfig(horizon=args.horizon, threshold=args.threshold),
        split_config=SplitConfig(),
    )
    run_optuna_time_series_search(
        data_config=data_config,
        optuna_config=OptunaConfig(
            study_name=args.study_name,
            n_trials=args.n_trials,
            seed=args.seed,
            reset_study=args.reset_study,
        ),
        training_config=TrainingConfig(epochs=args.optuna_epochs, early_stopping_patience=5, device=args.device),
        cv_gap=args.horizon,
    )
    run_top3_training_and_ensemble(
        data_config=data_config,
        optuna_config=OptunaConfig(study_name=args.study_name, seed=args.seed),
        training_config=TrainingConfig(epochs=args.final_epochs, early_stopping_patience=10, device=args.device),
        random_seed=args.seed,
        validation_gap=args.horizon,
    )
    evaluate_saved_predictions(data_config.features_parquet.parents[2])

    print("Full pipeline completed.")


if __name__ == "__main__":
    main()
