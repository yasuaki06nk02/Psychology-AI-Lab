from datetime import UTC, datetime
from uuid import uuid4

from app.domain.entities.dataset import Dataset
from app.domain.repositories.dataset_repository import DatasetRepository


class DatasetService:
    def __init__(self, repository: DatasetRepository) -> None:
        self._repository = repository

    def create(self, dataset_name: str, version: str, question_count: int) -> Dataset:
        dataset = Dataset(
            id=str(uuid4()),
            dataset_name=dataset_name,
            version=version,
            question_count=question_count,
            created_at=datetime.now(UTC),
        )
        return self._repository.save(dataset)

    def get(self, dataset_id: str) -> Dataset | None:
        return self._repository.get_by_id(dataset_id)

    def list(self) -> list[Dataset]:
        return self._repository.list_all()
