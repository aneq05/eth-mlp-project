import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader

from ..evaluation.metrics import compute_classification_metrics


@torch.no_grad()
def validate_one_epoch(
    model: nn.Module,
    dataloader: DataLoader,
    criterion: nn.Module,
    device: torch.device,
) -> dict[str, float]:
    model.eval()
    running_loss = 0.0
    num_batches = 0
    all_preds: list[np.ndarray] = []
    all_targets: list[np.ndarray] = []

    for x_batch, y_batch in dataloader:
        x_batch = x_batch.to(device)
        y_batch = y_batch.to(device)

        logits = model(x_batch)
        loss = criterion(logits, y_batch)

        preds = torch.argmax(logits, dim=1)
        all_preds.append(preds.cpu().numpy())
        all_targets.append(y_batch.cpu().numpy())

        running_loss += loss.item()
        num_batches += 1

    y_pred = np.concatenate(all_preds)
    y_true = np.concatenate(all_targets)
    metrics = compute_classification_metrics(y_true=y_true, y_pred=y_pred)
    metrics["val_loss"] = running_loss / max(1, num_batches)
    return metrics
