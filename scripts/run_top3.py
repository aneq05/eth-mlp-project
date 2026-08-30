import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.core.config import DataConfig, OptunaConfig, TrainingConfig
from src.core.utils import resolve_run_dir
from src.pipelines.train_top3 import run_top3_training_and_ensemble


def main() -> None:
    parser = argparse.ArgumentParser(description="Train top-3 Optuna models and evaluate ensemble.")
    parser.add_argument("--epochs", type=int, default=50, help="Epochs for final model training.")
    parser.add_argument("--patience", type=int, default=10, help="Early stopping patience.")
    parser.add_argument("--study-name", type=str, default="eth_mlp_optimization", help="Optuna study name.")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for final training.")
    parser.add_argument("--run-id", type=str, default=None, help="Run ID under reports/runs/.")
    parser.add_argument("--validation-gap", type=int, default=6, help="Purged gap for final train/validation split.")
    parser.add_argument("--corr-threshold", type=float, default=0.95, help="Final-training correlation threshold.")
    parser.add_argument("--no-vif", action="store_true", help="Disable final-training VIF reduction.")
    parser.add_argument("--vif-threshold", type=float, default=10.0, help="Final-training VIF threshold.")
    parser.add_argument("--device", type=str, default="cpu", help="Device, e.g. cpu or cuda.")
    args = parser.parse_args()

    training_config = TrainingConfig(
        epochs=args.epochs,
        early_stopping_patience=args.patience,
        device=args.device,
    )
    run_dir = resolve_run_dir(PROJECT_ROOT, args.run_id)

    summary = run_top3_training_and_ensemble(
        data_config=DataConfig(),
        optuna_config=OptunaConfig(study_name=args.study_name, seed=args.seed),
        training_config=training_config,
        random_seed=args.seed,
        validation_gap=args.validation_gap,
        corr_threshold=args.corr_threshold,
        apply_vif=not args.no_vif,
        vif_threshold=args.vif_threshold,
        run_dir=run_dir,
    )
    print("Top-3 training and ensemble evaluation completed.")
    print(f"Run directory: {run_dir}")
    print(summary)


if __name__ == "__main__":
    main()
