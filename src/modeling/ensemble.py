import numpy as np
from scipy.stats import entropy


def mean_probability_ensemble(model_probabilities: list[np.ndarray]) -> tuple[np.ndarray, np.ndarray]:
    stacked = np.stack(model_probabilities, axis=0)
    mean_probs = stacked.mean(axis=0)
    preds = mean_probs.argmax(axis=1)
    return mean_probs, preds


def majority_vote_ensemble(model_predictions: list[np.ndarray], num_classes: int = 3) -> np.ndarray:
    stacked = np.stack(model_predictions, axis=0)
    votes = []
    for i in range(stacked.shape[1]):
        counts = np.bincount(stacked[:, i], minlength=num_classes)
        votes.append(int(np.argmax(counts)))
    return np.array(votes, dtype=int)


def prediction_uncertainty(probabilities: np.ndarray) -> dict[str, np.ndarray]:
    ent = entropy(probabilities.T)
    sorted_probs = np.sort(probabilities, axis=1)
    margin = sorted_probs[:, -1] - sorted_probs[:, -2]
    return {"entropy": ent, "margin": margin}
