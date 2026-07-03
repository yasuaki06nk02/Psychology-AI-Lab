from datetime import UTC, datetime
from uuid import uuid4

from app.domain.entities.experiment import Experiment
from app.domain.repositories.experiment_repository import ExperimentRepository


class ExperimentService:
    def __init__(self, repository: ExperimentRepository) -> None:
        self._repository = repository

    def create(self, name: str, description: str) -> Experiment:
        experiment = Experiment(
            id=str(uuid4()),
            name=name,
            description=description,
            created_at=datetime.now(UTC),
        )
        return self._repository.save(experiment)

    def get(self, experiment_id: str) -> Experiment | None:
        return self._repository.get_by_id(experiment_id)

    def list(self) -> list[Experiment]:
        return self._repository.list_all()
