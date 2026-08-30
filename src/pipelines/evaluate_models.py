from pathlib import Path

import numpy as np
import pandas as pd

from ..core.utils import ensure_dir, save_json


def _compute_confusion_matrix(y_true: pd.Series, y_pred: pd.Series, labels: list[int]) -> np.ndarray:
    matrix = np.zeros((len(labels), len(labels)), dtype=int)
    label_to_idx = {label: idx for idx, label in enumerate(labels)}
    for actual, predicted in zip(y_true, y_pred, strict=False):
        if actual in label_to_idx and predicted in label_to_idx:
            matrix[label_to_idx[actual], label_to_idx[predicted]] += 1
    return matrix


def _compute_classification_report(y_true: pd.Series, y_pred: pd.Series, labels: list[int]) -> dict:
    try:
        from sklearn.metrics import classification_report

        return classification_report(y_true, y_pred, labels=labels, output_dict=True, zero_division=0)
    except ModuleNotFoundError:
        matrix = _compute_confusion_matrix(y_true, y_pred, labels)
        output: dict[str, dict | float] = {}
        total = int(matrix.sum())
        correct = int(np.trace(matrix))

        f1_scores = []
        supports = []
        for idx, label in enumerate(labels):
            tp = int(matrix[idx, idx])
            fp = int(matrix[:, idx].sum() - tp)
            fn = int(matrix[idx, :].sum() - tp)
            support = int(matrix[idx, :].sum())
            precision = tp / (tp + fp) if tp + fp else 0.0
            recall = tp / (tp + fn) if tp + fn else 0.0
            f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
            f1_scores.append(f1)
            supports.append(support)
            output[str(label)] = {
                "precision": precision,
                "recall": recall,
                "f1-score": f1,
                "support": support,
            }

        weights = np.array(supports, dtype=float)
        output["accuracy"] = correct / total if total else 0.0
        output["macro avg"] = {
            "precision": float(np.mean([output[str(label)]["precision"] for label in labels])),
            "recall": float(np.mean([output[str(label)]["recall"] for label in labels])),
            "f1-score": float(np.mean(f1_scores)),
            "support": total,
        }
        output["weighted avg"] = {
            "precision": float(np.average([output[str(label)]["precision"] for label in labels], weights=weights))
            if total
            else 0.0,
            "recall": float(np.average([output[str(label)]["recall"] for label in labels], weights=weights))
            if total
            else 0.0,
            "f1-score": float(np.average(f1_scores, weights=weights)) if total else 0.0,
            "support": total,
        }
        return output


def evaluate_saved_predictions(
    project_root: str | Path,
    run_dir: str | Path | None = None,
    predictions_dir: str | Path | None = None,
    make_figures: bool = True,
) -> dict:
    root = Path(project_root)
    output_dir = Path(run_dir) if run_dir is not None else root / "reports"
    predictions_path = Path(predictions_dir) if predictions_dir is not None else output_dir / "predictions"
    figures_dir = ensure_dir(output_dir / "figures") if make_figures else None

    files = sorted(predictions_path.glob("*_predictions.csv"))
    if not files:
        raise FileNotFoundError(f"No prediction files found in {predictions_path}. Run top-3 training first.")

    output: dict[str, dict] = {}
    for file_path in files:
        df = pd.read_csv(file_path)
        y_true = df["y_true"]
        y_pred = df["y_pred"]

        labels = [0, 1, 2]
        cm = _compute_confusion_matrix(y_true, y_pred, labels=labels)
        report = _compute_classification_report(y_true, y_pred, labels=labels)

        if make_figures:
            import matplotlib.pyplot as plt
            import seaborn as sns

            fig, ax = plt.subplots(figsize=(6, 5))
            sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
            ax.set_title(f"Confusion Matrix: {file_path.stem}")
            ax.set_xlabel("Predicted")
            ax.set_ylabel("True")
            fig.tight_layout()
            fig.savefig(figures_dir / f"{file_path.stem}_confusion_matrix.png", dpi=150)
            plt.close(fig)

        output[file_path.stem] = {"classification_report": report}

    save_json(output, output_dir / "evaluation_report.json")
    return output
