import argparse
import importlib
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, balanced_accuracy_score, classification_report, confusion_matrix, f1_score


def _import_neuralforecast():
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    blocked_paths = {script_dir.resolve(), repo_root.resolve()}

    cleaned_sys_path: list[str] = []
    for raw_path in sys.path:
        candidate = Path(raw_path or ".").resolve()
        if candidate not in blocked_paths:
            cleaned_sys_path.append(raw_path)
    sys.path = cleaned_sys_path

    try:
        nf_module = importlib.import_module("neuralforecast")
        models_module = importlib.import_module("neuralforecast.models")
    except Exception as exc:
        raise ImportError(
            "Could not import external package 'neuralforecast'. Install it with: pip install neuralforecast"
        ) from exc

    return nf_module.NeuralForecast, models_module.PatchTST


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Train PatchTST (NeuralForecast) on ETH data and evaluate sell/hold/buy accuracy."
    )
    parser.add_argument(
        "--raw-csv",
        type=str,
        default=None,
        help="Path to raw ETH CSV with at least timestamp and close columns. If set, splits are built automatically.",
    )
    parser.add_argument("--train-csv", type=str, default="data/labeled/train_labeled.csv")
    parser.add_argument("--val-csv", type=str, default="data/labeled/val_labeled.csv")
    parser.add_argument("--test-csv", type=str, default="data/labeled/test_labeled.csv")
    parser.add_argument("--horizon-hours", type=int, default=6, help="Horizon for future_return when raw CSV is used.")
    parser.add_argument("--threshold", type=float, default=0.0075, help="Class threshold for sell/hold/buy.")
    parser.add_argument("--train-ratio", type=float, default=0.70)
    parser.add_argument("--val-ratio", type=float, default=0.15)
    parser.add_argument("--test-ratio", type=float, default=0.15)
    parser.add_argument("--freq", type=str, default="h", help="Pandas offset alias for timestamp frequency.")
    parser.add_argument("--input-size", type=int, default=256)
    parser.add_argument("--patch-len", type=int, default=16)
    parser.add_argument("--stride", type=int, default=8)
    parser.add_argument("--hidden-size", type=int, default=128)
    parser.add_argument("--n-heads", type=int, default=8)
    parser.add_argument("--encoder-layers", type=int, default=3)
    parser.add_argument("--dropout", type=float, default=0.2)
    parser.add_argument("--learning-rate", type=float, default=1e-3)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--max-steps", type=int, default=1200)
    parser.add_argument("--val-check-steps", type=int, default=100)
    parser.add_argument("--early-stop-patience-steps", type=int, default=5)
    parser.add_argument("--scaler-type", type=str, default="robust")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output-dir", type=str, default="reports/neuralforecast")
    return parser.parse_args()


def assign_classes(returns: pd.Series, threshold: float) -> np.ndarray:
    values = returns.to_numpy(dtype=np.float64)
    classes = np.where(values > threshold, 2, np.where(values < -threshold, 0, 1))
    return classes.astype(np.int64)


def load_from_raw(
    raw_csv: Path,
    horizon_hours: int,
    train_ratio: float,
    val_ratio: float,
    test_ratio: float,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    if not np.isclose(train_ratio + val_ratio + test_ratio, 1.0):
        raise ValueError("train_ratio + val_ratio + test_ratio must sum to 1.0")

    df = pd.read_csv(raw_csv)
    required = {"timestamp", "close"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Raw CSV missing columns: {sorted(missing)}")

    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")
    df["close"] = pd.to_numeric(df["close"], errors="coerce")
    df = df.dropna(subset=["timestamp", "close"]).sort_values("timestamp").copy()
    df["future_return"] = (df["close"].shift(-horizon_hours) / df["close"]) - 1.0
    df = df.dropna(subset=["future_return"]).reset_index(drop=True)

    n = len(df)
    train_end = int(n * train_ratio)
    val_end = train_end + int(n * val_ratio)
    train_df = df.iloc[:train_end].copy()
    val_df = df.iloc[train_end:val_end].copy()
    test_df = df.iloc[val_end:].copy()
    return train_df, val_df, test_df


def load_from_split_files(train_csv: Path, val_csv: Path, test_csv: Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    train_df = pd.read_csv(train_csv)
    val_df = pd.read_csv(val_csv)
    test_df = pd.read_csv(test_csv)
    return train_df, val_df, test_df


def normalize_split(df: pd.DataFrame, split_name: str) -> pd.DataFrame:
    required = {"timestamp", "future_return"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"{split_name}: missing required columns {sorted(missing)}")

    out = df.copy()
    out["timestamp"] = pd.to_datetime(out["timestamp"], utc=True, errors="coerce")
    out["future_return"] = pd.to_numeric(out["future_return"], errors="coerce")
    out = out.dropna(subset=["timestamp", "future_return"]).sort_values("timestamp")
    out = out.drop_duplicates(subset=["timestamp"], keep="first")
    return out.reset_index(drop=True)


def main() -> None:
    args = parse_args()
    NeuralForecast, PatchTST = _import_neuralforecast()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.raw_csv:
        train_df, val_df, test_df = load_from_raw(
            raw_csv=Path(args.raw_csv),
            horizon_hours=args.horizon_hours,
            train_ratio=args.train_ratio,
            val_ratio=args.val_ratio,
            test_ratio=args.test_ratio,
        )
        data_source = "raw_csv"
    else:
        train_df, val_df, test_df = load_from_split_files(
            train_csv=Path(args.train_csv),
            val_csv=Path(args.val_csv),
            test_csv=Path(args.test_csv),
        )
        data_source = "prepared_splits"

    train_df = normalize_split(train_df, "train")
    val_df = normalize_split(val_df, "val")
    test_df = normalize_split(test_df, "test")

    train_val_df = pd.concat([train_df, val_df], axis=0, ignore_index=True)
    train_val_df = train_val_df.sort_values("timestamp").reset_index(drop=True)

    nf_train = train_val_df.rename(columns={"timestamp": "ds", "future_return": "y"})[["ds", "y"]].copy()
    nf_train["unique_id"] = "ETHUSDT"
    nf_train = nf_train[["unique_id", "ds", "y"]]

    h_test = len(test_df)
    if h_test <= 0:
        raise ValueError("Test split is empty after cleaning.")

    model = PatchTST(
        h=h_test,
        input_size=args.input_size,
        patch_len=args.patch_len,
        stride=args.stride,
        hidden_size=args.hidden_size,
        n_heads=args.n_heads,
        encoder_layers=args.encoder_layers,
        dropout=args.dropout,
        learning_rate=args.learning_rate,
        batch_size=args.batch_size,
        max_steps=args.max_steps,
        val_check_steps=args.val_check_steps,
        early_stop_patience_steps=args.early_stop_patience_steps,
        scaler_type=args.scaler_type,
        random_seed=args.seed,
    )

    nf = NeuralForecast(models=[model], freq=args.freq)
    val_size = min(len(val_df), len(nf_train) - 1)
    if val_size <= 0:
        raise ValueError("Validation split is too short. Need at least 1 validation row for training.")
    nf.fit(df=nf_train, val_size=val_size, verbose=True)
    forecasts = nf.predict().reset_index(drop=False)

    pred_col_candidates = [c for c in forecasts.columns if c not in {"unique_id", "ds"}]
    if not pred_col_candidates:
        raise ValueError("Could not find prediction column in NeuralForecast output.")
    pred_col = pred_col_candidates[0]

    pred_df = forecasts[["ds", pred_col]].copy()
    pred_df = pred_df.rename(columns={pred_col: "pred_future_return"})
    pred_df["ds"] = pd.to_datetime(pred_df["ds"], utc=True, errors="coerce")

    test_eval = test_df.copy()
    test_eval["ds"] = pd.to_datetime(test_eval["timestamp"], utc=True, errors="coerce")
    merged = test_eval.merge(pred_df, on="ds", how="inner").sort_values("ds").reset_index(drop=True)
    if merged.empty:
        raise ValueError("No overlapping timestamps between forecast output and test split.")

    y_true = assign_classes(merged["future_return"], threshold=args.threshold)
    y_pred = assign_classes(merged["pred_future_return"], threshold=args.threshold)

    metrics = {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)),
        "f1_macro": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
        "n_test_rows_requested": int(len(test_df)),
        "n_test_rows_evaluated": int(len(merged)),
        "model": "PatchTST",
        "data_source": data_source,
        "threshold": float(args.threshold),
        "horizon_hours_for_labels": int(args.horizon_hours),
        "prediction_column": pred_col,
    }

    class_report = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1, 2]).tolist()

    metrics_path = output_dir / "patchtst_metrics.json"
    report_path = output_dir / "patchtst_classification_report.json"
    pred_path = output_dir / "patchtst_test_predictions.csv"
    cm_path = output_dir / "patchtst_confusion_matrix.json"

    merged_out = merged[["ds", "future_return", "pred_future_return"]].copy()
    merged_out["y_true_class"] = y_true
    merged_out["y_pred_class"] = y_pred
    merged_out.to_csv(pred_path, index=False)

    with metrics_path.open("w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=True, indent=2)
    with report_path.open("w", encoding="utf-8") as f:
        json.dump(class_report, f, ensure_ascii=True, indent=2)
    with cm_path.open("w", encoding="utf-8") as f:
        json.dump({"labels": [0, 1, 2], "matrix": cm}, f, ensure_ascii=True, indent=2)

    print("PatchTST training + evaluation finished.")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(f"Balanced Accuracy: {metrics['balanced_accuracy']:.4f}")
    print(f"F1 Macro: {metrics['f1_macro']:.4f}")
    print(f"Saved: {metrics_path}")
    print(f"Saved: {pred_path}")


if __name__ == "__main__":
    main()
