import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.core.config import PROJECT_ROOT
from src.pipelines.evaluate_models import evaluate_saved_predictions


def main() -> None:
    report = evaluate_saved_predictions(PROJECT_ROOT)
    print("Evaluation report generated.")
    print(report.keys())


if __name__ == "__main__":
    main()
