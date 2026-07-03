from app.application.providers.provider_bootstrap import create_provider_manager
from app.infrastructure.config.settings import Settings


def test_provider_bootstrap_registers_gemini_when_configured() -> None:
    settings = Settings(
        openai_api_key="",
        gemini_api_key="test-gemini-key",
    )

    manager = create_provider_manager(settings)

    assert "mock" in manager.list_providers()
    assert "gemini" in manager.list_providers()
