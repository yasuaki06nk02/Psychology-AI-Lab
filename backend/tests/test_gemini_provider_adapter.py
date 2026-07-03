import json

import httpx
import pytest

from app.application.errors import AppError
from app.application.providers.interfaces import ProviderRequest
from app.infrastructure.providers.gemini_provider_adapter import GeminiProviderAdapter


def test_gemini_adapter_lists_models() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/models"):
            return httpx.Response(
                200,
                json={
                    "models": [
                        {"name": "models/gemini-2.0-flash"},
                        {"name": "models/gemini-1.5-pro"},
                    ]
                },
            )
        return httpx.Response(404, json={})

    client = httpx.Client(transport=httpx.MockTransport(handler), timeout=1.0)
    adapter = GeminiProviderAdapter(
        api_key="test",
        base_url="https://generativelanguage.googleapis.com/v1beta",
        timeout_seconds=1.0,
        client=client,
    )

    assert adapter.list_models() == ["gemini-2.0-flash", "gemini-1.5-pro"]


def test_gemini_adapter_executes_prompt() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith(":generateContent"):
            payload = {
                "candidates": [
                    {
                        "content": {"parts": [{"text": "4"}]},
                        "finishReason": "STOP",
                    }
                ],
                "usageMetadata": {
                    "promptTokenCount": 10,
                    "candidatesTokenCount": 1,
                },
            }
            return httpx.Response(200, content=json.dumps(payload))
        return httpx.Response(404, json={})

    client = httpx.Client(transport=httpx.MockTransport(handler), timeout=1.0)
    adapter = GeminiProviderAdapter(
        api_key="test",
        base_url="https://generativelanguage.googleapis.com/v1beta",
        timeout_seconds=1.0,
        client=client,
    )

    response = adapter.execute_prompt(
        ProviderRequest(
            model_name="gemini-2.0-flash",
            system_prompt="system",
            developer_prompt="developer",
            user_prompt="2+2?",
        )
    )

    assert response.provider_name == "gemini"
    assert response.content == "4"
    assert response.input_tokens == 10
    assert response.output_tokens == 1


def test_gemini_adapter_maps_rate_limit_to_app_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith(":generateContent"):
            return httpx.Response(
                429,
                headers={"X-RateLimit-Reset": "1783123200000"},
                json={"error": {"message": "Rate limit exceeded", "code": 429}},
            )
        return httpx.Response(404, json={})

    client = httpx.Client(transport=httpx.MockTransport(handler), timeout=1.0)
    adapter = GeminiProviderAdapter(
        api_key="test",
        base_url="https://generativelanguage.googleapis.com/v1beta",
        timeout_seconds=1.0,
        client=client,
    )

    with pytest.raises(AppError) as exc_info:
        adapter.execute_prompt(
            ProviderRequest(
                model_name="gemini-2.0-flash",
                system_prompt="system",
                developer_prompt="developer",
                user_prompt="2+2?",
            )
        )

    assert exc_info.value.code == "provider_rate_limit"
    assert exc_info.value.status_code == 429
