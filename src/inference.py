import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader


@torch.no_grad()
def predict_probabilities(model: nn.Module, dataloader: DataLoader, device: torch.device) -> np.ndarray:
    model.eval()
    model.to(device)
    probs_list: list[np.ndarray] = []
    for x_batch, _ in dataloader:
        x_batch = x_batch.to(device)
        logits = model(x_batch)
        probs = torch.softmax(logits, dim=1)
        probs_list.append(probs.cpu().numpy())
    return np.concatenate(probs_list, axis=0)


def predict_classes(probabilities: np.ndarray) -> np.ndarray:
    return probabilities.argmax(axis=1)
