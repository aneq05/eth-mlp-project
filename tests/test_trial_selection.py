from dataclasses import dataclass
from unittest import TestCase

from src.modeling.trial_selection import select_top_completed_trials


@dataclass
class FakeState:
    name: str


@dataclass
class FakeTrial:
    number: int
    value: float | None
    state: FakeState


class TestSelectTopCompletedTrials(TestCase):
    def test_selects_only_completed_trials_with_values(self) -> None:
        trials = [
            FakeTrial(number=0, value=0.3, state=FakeState("COMPLETE")),
            FakeTrial(number=1, value=0.5, state=FakeState("PRUNED")),
            FakeTrial(number=2, value=None, state=FakeState("COMPLETE")),
            FakeTrial(number=3, value=0.4, state=FakeState("COMPLETE")),
        ]

        selected = select_top_completed_trials(trials, limit=3, direction="maximize")

        self.assertEqual([trial.number for trial in selected], [3, 0])

    def test_sorts_minimize_direction(self) -> None:
        trials = [
            FakeTrial(number=0, value=0.3, state=FakeState("COMPLETE")),
            FakeTrial(number=1, value=0.2, state=FakeState("COMPLETE")),
            FakeTrial(number=2, value=0.4, state=FakeState("COMPLETE")),
        ]

        selected = select_top_completed_trials(trials, limit=2, direction="minimize")

        self.assertEqual([trial.number for trial in selected], [1, 0])

    def test_uses_trial_number_as_tie_breaker(self) -> None:
        trials = [
            FakeTrial(number=3, value=0.5, state=FakeState("COMPLETE")),
            FakeTrial(number=1, value=0.5, state=FakeState("COMPLETE")),
        ]

        selected = select_top_completed_trials(trials, limit=2, direction="maximize")

        self.assertEqual([trial.number for trial in selected], [1, 3])
