from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix

from ..core.utils import ensure_dir, save_json


def evaluate_saved_predictions(project_root: str | Path) -> dict:
    root = Path(project_root)
    predictions_dir = root / "reports" / "predictions"
    figures_dir = ensure_dir(root / "reports" / "figures")

    files = sorted(predictions_dir.glob("*_predictions.csv"))
    if not files:
        raise FileNotFoundError("No prediction files found. Run top-3 training first.")

    output: dict[str, dict] = {}
    for file_path in files:
        df = pd.read_csv(file_path)
        y_true = df["y_true"]
        y_pred = df["y_pred"]

        cm = confusion_matrix(y_true, y_pred, labels=[0, 1, 2])
        report = classification_report(y_true, y_pred, labels=[0, 1, 2], output_dict=True, zero_division=0)

        fig, ax = plt.subplots(figsize=(6, 5))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
        ax.set_title(f"Confusion Matrix: {file_path.stem}")
        ax.set_xlabel("Predicted")
        ax.set_ylabel("True")
        fig.tight_layout()
        fig.savefig(figures_dir / f"{file_path.stem}_confusion_matrix.png", dpi=150)
        plt.close(fig)

        output[file_path.stem] = {"classification_report": report}

    save_json(output, root / "reports" / "evaluation_report.json")
    return output
