import json

import httpx
import pytest

from app.application.errors import AppError
from app.application.providers.interfaces import ProviderRequest
from app.infrastructure.providers.openai_provider_adapter import OpenAIProviderAdapter


def test_openai_adapter_lists_models() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/models"):
            return httpx.Response(200, json={"data": [{"id": "gpt-4o-mini"}]})
        return httpx.Response(404, json={})

    client = httpx.Client(transport=httpx.MockTransport(handler), timeout=1.0)
    adapter = OpenAIProviderAdapter(
        api_key="test",
        base_url="https://api.openai.com/v1",
        timeout_seconds=1.0,
        client=client,
    )

    assert adapter.list_models() == ["gpt-4o-mini"]


def test_openai_adapter_executes_prompt() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/chat/completions"):
            payload = {
                "model": "gpt-4o-mini-2026-07-01",
                "choices": [
                    {
                        "message": {"content": "4"},
                        "finish_reason": "stop",
                    }
                ],
                "usage": {"prompt_tokens": 12, "completion_tokens": 1},
            }
            return httpx.Response(200, content=json.dumps(payload))
        return httpx.Response(404, json={})

    client = httpx.Client(transport=httpx.MockTransport(handler), timeout=1.0)
    adapter = OpenAIProviderAdapter(
        api_key="test",
        base_url="https://api.openai.com/v1",
        timeout_seconds=1.0,
        client=client,
    )

    response = adapter.execute_prompt(
        ProviderRequest(
            model_name="gpt-4o-mini",
            system_prompt="system",
            developer_prompt="developer",
            user_prompt="2+2?",
        )
    )

    assert response.provider_name == "openai"
    assert response.content == "4"
    assert response.input_tokens == 12
    assert response.output_tokens == 1


def test_openai_adapter_supports_custom_provider_name() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/chat/completions"):
            payload = {
                "model": "gpt-4.1",
                "choices": [{"message": {"content": "ok"}, "finish_reason": "stop"}],
                "usage": {"prompt_tokens": 1, "completion_tokens": 1},
            }
            return httpx.Response(200, content=json.dumps(payload))
        return httpx.Response(404, json={})

    client = httpx.Client(transport=httpx.MockTransport(handler), timeout=1.0)
    adapter = OpenAIProviderAdapter(
        name="copilot",
        api_key="test",
        base_url="https://models.inference.ai.azure.com",
        timeout_seconds=1.0,
        client=client,
    )

    assert adapter.name == "copilot"

    response = adapter.execute_prompt(
        ProviderRequest(
            model_name="gpt-4.1",
            system_prompt="system",
            developer_prompt="developer",
            user_prompt="ping",
        )
    )

    assert response.provider_name == "copilot"


def test_openai_adapter_maps_rate_limit_to_app_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/chat/completions"):
            return httpx.Response(
                429,
                headers={"X-RateLimit-Reset": "1783123200000"},
                json={"error": {"message": "Rate limit exceeded", "code": 429}},
            )
        return httpx.Response(404, json={})

    client = httpx.Client(transport=httpx.MockTransport(handler), timeout=1.0)
    adapter = OpenAIProviderAdapter(
        api_key="test",
        base_url="https://api.openai.com/v1",
        timeout_seconds=1.0,
        client=client,
    )

    with pytest.raises(AppError) as exc_info:
        adapter.execute_prompt(
            ProviderRequest(
                model_name="gpt-4o-mini",
                system_prompt="system",
                developer_prompt="developer",
                user_prompt="2+2?",
            )
        )

    assert exc_info.value.code == "provider_rate_limit"
    assert exc_info.value.status_code == 429
