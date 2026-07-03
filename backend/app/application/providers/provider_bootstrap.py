from app.application.providers.provider_manager import ProviderManager
from app.application.providers.provider_registry import ProviderRegistry
from app.infrastructure.config.settings import Settings
from app.infrastructure.providers.gemini_provider_adapter import GeminiProviderAdapter
from app.infrastructure.providers.mock_provider_adapter import MockProviderAdapter
from app.infrastructure.providers.openai_provider_adapter import OpenAIProviderAdapter


def create_provider_manager(settings: Settings) -> ProviderManager:
    registry = ProviderRegistry()

    # Keep mock adapter for deterministic local tests and offline operation.
    registry.register(MockProviderAdapter(name="mock"))

    if settings.openai_api_key:
        registry.register(
            OpenAIProviderAdapter(
                name="openai",
                api_key=settings.openai_api_key,
                base_url=settings.openai_base_url,
                timeout_seconds=settings.provider_timeout_seconds,
            )
        )

    if settings.copilot_api_key:
        registry.register(
            OpenAIProviderAdapter(
                name="copilot",
                api_key=settings.copilot_api_key,
                base_url=settings.copilot_base_url,
                timeout_seconds=settings.provider_timeout_seconds,
            )
        )

    if settings.gemini_api_key:
        registry.register(
            GeminiProviderAdapter(
                api_key=settings.gemini_api_key,
                base_url=settings.gemini_base_url,
                timeout_seconds=settings.provider_timeout_seconds,
            )
        )

    return ProviderManager(registry)
