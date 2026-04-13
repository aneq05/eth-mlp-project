from pathlib import Path

import pandas as pd


def load_ohlcv_csv(csv_path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    required_cols = {"timestamp", "open", "high", "low", "close", "volume"}
    missing_cols = required_cols.difference(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns: {sorted(missing_cols)}")
    return df


def save_dataframe(df: pd.DataFrame, output_path: str | Path) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.suffix.lower() == ".parquet":
        df.to_parquet(output_path, index=True)
    elif output_path.suffix.lower() == ".csv":
        df.to_csv(output_path, index=True)
    else:
        raise ValueError(f"Unsupported output format: {output_path.suffix}")
