import pytest

from app.application.errors import AppError
from app.application.providers.provider_manager import ProviderManager
from app.application.providers.provider_registry import ProviderRegistry
from app.infrastructure.providers.mock_provider_adapter import MockProviderAdapter


def test_provider_manager_uses_registry() -> None:
    registry = ProviderRegistry()
    registry.register(MockProviderAdapter(name="mock"))
    manager = ProviderManager(registry)

    assert manager.list_providers() == ["mock"]
    assert manager.health_check("mock") is True
    assert manager.list_models("mock") == ["mock-model-v1"]


def test_provider_manager_raises_not_found() -> None:
    manager = ProviderManager(ProviderRegistry())

    with pytest.raises(AppError) as exc_info:
        manager.list_models("missing")

    assert exc_info.value.code == "provider_not_found"
