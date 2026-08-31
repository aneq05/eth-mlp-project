import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.core.config import DataConfig
from src.core.utils import resolve_run_dir
from src.pipelines.train_baselines import run_baseline_models


def main() -> None:
    parser = argparse.ArgumentParser(description="Train simple baseline models for one prepared run.")
    parser.add_argument("--run-id", type=str, required=True, help="Run ID under reports/runs/.")
    parser.add_argument("--corr-threshold", type=float, default=0.95, help="Baseline correlation threshold.")
    parser.add_argument("--use-vif", action="store_true", help="Enable VIF reduction for baseline models.")
    parser.add_argument("--vif-threshold", type=float, default=10.0, help="Baseline VIF threshold.")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for baseline models.")
    args = parser.parse_args()

    run_dir = resolve_run_dir(PROJECT_ROOT, args.run_id)
    summary = run_baseline_models(
        data_config=DataConfig().with_run_dir(run_dir),
        corr_threshold=args.corr_threshold,
        apply_vif=args.use_vif,
        vif_threshold=args.vif_threshold,
        random_seed=args.seed,
        run_dir=run_dir,
    )
    print("Baseline models completed.")
    print(f"Run directory: {run_dir}")
    print(summary)


if __name__ == "__main__":
    main()
