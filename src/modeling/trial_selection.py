def select_top_completed_trials(trials, limit: int, direction: str = "maximize") -> list:
    if limit <= 0:
        raise ValueError("limit must be a positive integer")
    if direction not in {"maximize", "minimize"}:
        raise ValueError("direction must be either 'maximize' or 'minimize'")

    completed = []
    for trial in trials:
        state = getattr(trial, "state", None)
        state_name = getattr(state, "name", str(state))
        value = getattr(trial, "value", None)
        if state_name == "COMPLETE" and value is not None:
            completed.append(trial)

    if direction == "maximize":
        return sorted(completed, key=lambda trial: (-float(trial.value), int(getattr(trial, "number", 0))))[:limit]
    return sorted(completed, key=lambda trial: (float(trial.value), int(getattr(trial, "number", 0))))[:limit]
