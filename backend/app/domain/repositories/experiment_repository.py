from typing import Protocol

from app.domain.entities.experiment import Experiment


class ExperimentRepository(Protocol):
    def save(self, experiment: Experiment) -> Experiment: ...

    def get_by_id(self, experiment_id: str) -> Experiment | None: ...

    def list_all(self) -> list[Experiment]: ...
