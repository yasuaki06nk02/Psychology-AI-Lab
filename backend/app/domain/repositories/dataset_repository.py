from typing import Protocol

from app.domain.entities.dataset import Dataset


class DatasetRepository(Protocol):
    def save(self, dataset: Dataset) -> Dataset: ...

    def get_by_id(self, dataset_id: str) -> Dataset | None: ...

    def list_all(self) -> list[Dataset]: ...
