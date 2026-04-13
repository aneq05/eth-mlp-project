import numpy as np
import torch


def compute_class_weights(y: np.ndarray, num_classes: int = 3) -> torch.Tensor:
    counts = np.bincount(y.astype(int), minlength=num_classes).astype(float)
    counts[counts == 0] = 1.0
    weights = counts.sum() / (num_classes * counts)
    return torch.tensor(weights, dtype=torch.float32)
