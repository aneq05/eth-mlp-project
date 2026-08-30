import json
import random
from datetime import UTC, datetime
from pathlib import Path

import numpy as np


def set_seed(seed: int = 42) -> None:
    import torch

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def ensure_dir(path: str | Path) -> Path:
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def make_run_id(seed: int | None = None) -> str:
    timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
    suffix = f"_seed{seed}" if seed is not None else ""
    return f"run_{timestamp}{suffix}"


def resolve_run_dir(project_root: str | Path, run_id: str | None = None) -> Path:
    root = Path(project_root)
    if run_id is None:
        run_id = make_run_id()
    return ensure_dir(root / "reports" / "runs" / run_id)


def save_json(data: dict, output_path: str | Path) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_json(input_path: str | Path) -> dict:
    with Path(input_path).open("r", encoding="utf-8") as f:
        return json.load(f)
