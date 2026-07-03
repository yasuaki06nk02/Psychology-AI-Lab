from app.application.providers.interfaces import ProviderAdapter


class ProviderRegistry:
    def __init__(self) -> None:
        self._providers: dict[str, ProviderAdapter] = {}

    def register(self, provider: ProviderAdapter) -> None:
        self._providers[provider.name] = provider

    def get(self, provider_name: str) -> ProviderAdapter | None:
        return self._providers.get(provider_name)

    def list_names(self) -> list[str]:
        return list(self._providers.keys())
