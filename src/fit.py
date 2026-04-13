from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from .train import train_one_epoch
from .validate import validate_one_epoch


def _is_improvement(curr: float, best: float, mode: str) -> bool:
    if mode == "max":
        return curr > best
    if mode == "min":
        return curr < best
    raise ValueError(f"Unsupported mode: {mode}")


def fit_model(
    model: nn.Module,
    train_loader: DataLoader,
    val_loader: DataLoader,
    criterion: nn.Module,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
    epochs: int,
    checkpoint_path: str | Path,
    tensorboard_log_dir: str | Path,
    monitor_metric: str = "f1_macro",
    monitor_mode: str = "max",
    early_stopping_patience: int = 10,
    clip_grad_norm: float | None = 1.0,
) -> dict[str, list[float]]:
    checkpoint_path = Path(checkpoint_path)
    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
    writer = SummaryWriter(log_dir=str(tensorboard_log_dir))

    history: dict[str, list[float]] = {
        "train_loss": [],
        "val_loss": [],
        "f1_macro": [],
        "balanced_accuracy": [],
        "accuracy": [],
    }

    best_score = float("-inf") if monitor_mode == "max" else float("inf")
    best_epoch = -1

    model.to(device)

    for epoch in range(1, epochs + 1):
        train_metrics = train_one_epoch(
            model=model,
            dataloader=train_loader,
            criterion=criterion,
            optimizer=optimizer,
            device=device,
            clip_grad_norm=clip_grad_norm,
        )
        val_metrics = validate_one_epoch(
            model=model,
            dataloader=val_loader,
            criterion=criterion,
            device=device,
        )

        history["train_loss"].append(train_metrics["train_loss"])
        history["val_loss"].append(val_metrics["val_loss"])
        history["f1_macro"].append(val_metrics["f1_macro"])
        history["balanced_accuracy"].append(val_metrics["balanced_accuracy"])
        history["accuracy"].append(val_metrics["accuracy"])

        writer.add_scalar("loss/train", train_metrics["train_loss"], epoch)
        writer.add_scalar("loss/val", val_metrics["val_loss"], epoch)
        writer.add_scalar("metrics/f1_macro", val_metrics["f1_macro"], epoch)
        writer.add_scalar("metrics/balanced_accuracy", val_metrics["balanced_accuracy"], epoch)
        writer.add_scalar("metrics/accuracy", val_metrics["accuracy"], epoch)
        writer.add_scalar("optim/lr", optimizer.param_groups[0]["lr"], epoch)

        monitored_value = val_metrics[monitor_metric]
        if _is_improvement(monitored_value, best_score, mode=monitor_mode):
            best_score = monitored_value
            best_epoch = epoch
            torch.save(
                {
                    "epoch": epoch,
                    "model_state_dict": model.state_dict(),
                    "optimizer_state_dict": optimizer.state_dict(),
                    "best_score": best_score,
                    "monitor_metric": monitor_metric,
                },
                checkpoint_path,
            )

        if epoch - best_epoch >= early_stopping_patience:
            break

    writer.close()
    return history
