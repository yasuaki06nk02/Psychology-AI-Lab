from app.application.errors import AppError
from app.application.providers.interfaces import ProviderRequest, ProviderResponse
from app.application.providers.provider_registry import ProviderRegistry


class ProviderManager:
    def __init__(self, registry: ProviderRegistry) -> None:
        self._registry = registry

    def list_providers(self) -> list[str]:
        return self._registry.list_names()

    def list_models(self, provider_name: str) -> list[str]:
        provider = self._registry.get(provider_name)
        if provider is None:
            raise AppError("provider_not_found", f"Provider '{provider_name}' is not registered", 404)
        return provider.list_models()

    def health_check(self, provider_name: str) -> bool:
        provider = self._registry.get(provider_name)
        if provider is None:
            raise AppError("provider_not_found", f"Provider '{provider_name}' is not registered", 404)
        return provider.health_check()

    def execute_prompt(self, provider_name: str, request: ProviderRequest) -> ProviderResponse:
        provider = self._registry.get(provider_name)
        if provider is None:
            raise AppError("provider_not_found", f"Provider '{provider_name}' is not registered", 404)
        try:
            return provider.execute_prompt(request)
        except AppError:
            raise
        except TimeoutError as exc:
            raise AppError("provider_timeout", str(exc), 504) from exc
        except ConnectionError as exc:
            raise AppError("provider_connection_error", str(exc), 503) from exc
        except Exception as exc:  # pragma: no cover
            raise AppError("provider_execution_error", str(exc), 502) from exc
