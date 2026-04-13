import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.core.config import DataConfig, OptunaConfig, TrainingConfig
from src.pipelines.train_top3 import run_top3_training_and_ensemble


def main() -> None:
    parser = argparse.ArgumentParser(description="Train top-3 Optuna models and evaluate ensemble.")
    parser.add_argument("--epochs", type=int, default=50, help="Epochs for final model training.")
    parser.add_argument("--patience", type=int, default=10, help="Early stopping patience.")
    parser.add_argument("--device", type=str, default="cpu", help="Device, e.g. cpu or cuda.")
    args = parser.parse_args()

    training_config = TrainingConfig(
        epochs=args.epochs,
        early_stopping_patience=args.patience,
        device=args.device,
    )

    summary = run_top3_training_and_ensemble(
        data_config=DataConfig(),
        optuna_config=OptunaConfig(),
        training_config=training_config,
    )
    print("Top-3 training and ensemble evaluation completed.")
    print(summary)


if __name__ == "__main__":
    main()
