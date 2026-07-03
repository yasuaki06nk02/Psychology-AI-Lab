from typing import Protocol

from app.domain.entities.provider import Provider


class ProviderRepository(Protocol):
    def save(self, provider: Provider) -> Provider: ...

    def get_by_id(self, provider_id: str) -> Provider | None: ...

    def list_all(self) -> list[Provider]: ...
