import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.core.config import DataConfig, SplitConfig, TargetConfig
from src.core.utils import resolve_run_dir
from src.pipelines.prepare_data import prepare_datasets


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare ETH datasets: clean -> features -> target -> split.")
    parser.add_argument("--raw-csv", type=str, default=None, help="Path to raw ETHUSDT 1h CSV.")
    parser.add_argument("--horizon", type=int, default=6, help="Prediction horizon in hours.")
    parser.add_argument("--threshold", type=float, default=0.0075, help="Target threshold (tau).")
    parser.add_argument("--run-id", type=str, default=None, help="Run ID under reports/runs/.")
    args = parser.parse_args()
    run_dir = resolve_run_dir(PROJECT_ROOT, args.run_id)

    data_config = DataConfig()
    if args.raw_csv:
        data_config.raw_csv = args.raw_csv
    data_config = data_config.with_run_dir(run_dir)

    metadata = prepare_datasets(
        data_config=data_config,
        target_config=TargetConfig(horizon=args.horizon, threshold=args.threshold),
        split_config=SplitConfig(),
        output_dir=run_dir,
    )
    print("Data preparation completed.")
    print(f"Run directory: {run_dir}")
    print(metadata)


if __name__ == "__main__":
    main()
