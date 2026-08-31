import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.core.config import PROJECT_ROOT
from src.pipelines.evaluate_models import evaluate_saved_predictions


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate saved prediction files for one run.")
    parser.add_argument("--run-id", type=str, default=None, help="Run ID under reports/runs/.")
    parser.add_argument("--predictions-dir", type=str, default=None, help="Explicit predictions directory.")
    parser.add_argument("--no-figures", action="store_true", help="Skip confusion matrix PNG generation.")
    args = parser.parse_args()
    if args.run_id is None and args.predictions_dir is None:
        raise SystemExit("--run-id is required unless --predictions-dir is provided.")

    run_dir = PROJECT_ROOT / "reports" / "runs" / args.run_id if args.run_id else None
    report = evaluate_saved_predictions(
        PROJECT_ROOT,
        run_dir=run_dir,
        predictions_dir=args.predictions_dir,
        make_figures=not args.no_figures,
    )
    print("Evaluation report generated.")
    print(report.keys())


if __name__ == "__main__":
    main()
