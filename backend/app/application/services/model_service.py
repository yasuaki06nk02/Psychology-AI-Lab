from datetime import UTC, datetime
from uuid import uuid4

from app.domain.entities.model import AIModel
from app.domain.repositories.model_repository import ModelRepository


class ModelService:
    def __init__(self, repository: ModelRepository) -> None:
        self._repository = repository

    def create(self, provider_id: str, model_name: str, version: str) -> AIModel:
        model = AIModel(
            id=str(uuid4()),
            provider_id=provider_id,
            model_name=model_name,
            version=version,
            created_at=datetime.now(UTC),
        )
        return self._repository.save(model)

    def get(self, model_id: str) -> AIModel | None:
        return self._repository.get_by_id(model_id)

    def list(self) -> list[AIModel]:
        return self._repository.list_all()
