from dataclasses import dataclass, field
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


@dataclass
class DataConfig:
    raw_csv: Path = PROJECT_ROOT / "data" / "raw" / "ethusdt_1h.csv"
    clean_csv: Path = PROJECT_ROOT / "data" / "interim" / "eth_clean.csv"
    features_parquet: Path = PROJECT_ROOT / "data" / "processed" / "features.parquet"
    train_parquet: Path = PROJECT_ROOT / "data" / "processed" / "train.parquet"
    val_parquet: Path = PROJECT_ROOT / "data" / "processed" / "val.parquet"
    test_parquet: Path = PROJECT_ROOT / "data" / "processed" / "test.parquet"


@dataclass
class TargetConfig:
    horizon: int = 6
    threshold: float = 0.0075
    sell_label: int = 0
    hold_label: int = 1
    buy_label: int = 2


@dataclass
class SplitConfig:
    train_ratio: float = 0.70
    val_ratio: float = 0.15
    test_ratio: float = 0.15
    n_splits_cv: int = 5


@dataclass
class ModelConfig:
    input_dim: int = 32
    hidden_dims: list[int] = field(default_factory=lambda: [256, 128, 64])
    num_classes: int = 3
    activation: str = "gelu"
    dropout: float = 0.2
    use_batchnorm: bool = True


@dataclass
class TrainingConfig:
    epochs: int = 50
    batch_size: int = 128
    lr: float = 1e-3
    weight_decay: float = 1e-5
    clip_grad_norm: float = 1.0
    early_stopping_patience: int = 10
    monitor_metric: str = "f1_macro"
    monitor_mode: str = "max"
    num_workers: int = 0
    device: str = "cpu"


@dataclass
class OptunaConfig:
    study_name: str = "eth_mlp_optimization"
    direction: str = "maximize"
    n_trials: int = 30
    timeout_seconds: int | None = None
    storage_url: str = f"sqlite:///{PROJECT_ROOT / 'logs' / 'optuna' / 'optuna.db'}"
