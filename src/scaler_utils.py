import numpy as np
from sklearn.preprocessing import RobustScaler, StandardScaler


def get_scaler(scaler_type: str = "standard"):
    scaler_type = scaler_type.lower()
    if scaler_type == "standard":
        return StandardScaler()
    if scaler_type == "robust":
        return RobustScaler()
    raise ValueError(f"Unsupported scaler_type: {scaler_type}")


def fit_transform_train_val(
    x_train: np.ndarray,
    x_val: np.ndarray,
    scaler_type: str = "standard",
) -> tuple[np.ndarray, np.ndarray, object]:
    scaler = get_scaler(scaler_type=scaler_type)
    x_train_scaled = scaler.fit_transform(x_train)
    x_val_scaled = scaler.transform(x_val)
    return x_train_scaled, x_val_scaled, scaler
