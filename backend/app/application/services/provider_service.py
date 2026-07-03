from datetime import UTC, datetime
from uuid import uuid4

from app.domain.entities.provider import Provider
from app.domain.repositories.provider_repository import ProviderRepository


class ProviderService:
    def __init__(self, repository: ProviderRepository) -> None:
        self._repository = repository

    def create(self, name: str, display_name: str) -> Provider:
        provider = Provider(
            id=str(uuid4()),
            name=name,
            display_name=display_name,
            created_at=datetime.now(UTC),
        )
        return self._repository.save(provider)

    def get(self, provider_id: str) -> Provider | None:
        return self._repository.get_by_id(provider_id)

    def list(self) -> list[Provider]:
        return self._repository.list_all()
