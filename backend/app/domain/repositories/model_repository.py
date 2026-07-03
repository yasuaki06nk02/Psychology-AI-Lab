from typing import Protocol

from app.domain.entities.model import AIModel


class ModelRepository(Protocol):
    def save(self, model: AIModel) -> AIModel: ...

    def get_by_id(self, model_id: str) -> AIModel | None: ...

    def list_all(self) -> list[AIModel]: ...
