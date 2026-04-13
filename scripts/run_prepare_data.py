import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.core.config import DataConfig, SplitConfig, TargetConfig
from src.pipelines.prepare_data import prepare_datasets


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare ETH datasets: clean -> features -> target -> split.")
    parser.add_argument("--raw-csv", type=str, default=None, help="Path to raw ETHUSDT 1h CSV.")
    parser.add_argument("--horizon", type=int, default=6, help="Prediction horizon in hours.")
    parser.add_argument("--threshold", type=float, default=0.0075, help="Target threshold (tau).")
    parser.add_argument("--corr-threshold", type=float, default=0.95, help="Correlation threshold.")
    parser.add_argument("--no-vif", action="store_true", help="Disable VIF-based reduction.")
    parser.add_argument("--vif-threshold", type=float, default=10.0, help="VIF threshold.")
    args = parser.parse_args()

    data_config = DataConfig()
    if args.raw_csv:
        data_config.raw_csv = args.raw_csv

    metadata = prepare_datasets(
        data_config=data_config,
        target_config=TargetConfig(horizon=args.horizon, threshold=args.threshold),
        split_config=SplitConfig(),
        corr_threshold=args.corr_threshold,
        apply_vif=not args.no_vif,
        vif_threshold=args.vif_threshold,
    )
    print("Data preparation completed.")
    print(metadata)


if __name__ == "__main__":
    main()
