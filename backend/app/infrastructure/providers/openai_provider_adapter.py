from __future__ import annotations

import json
from datetime import UTC, datetime
from time import perf_counter

import httpx

from app.application.errors import AppError
from app.application.providers.interfaces import (
    ProviderAdapter,
    ProviderRequest,
    ProviderResponse,
)


class OpenAIProviderAdapter(ProviderAdapter):
    def __init__(
        self,
        *,
        name: str = "openai",
        api_key: str,
        base_url: str,
        timeout_seconds: float,
        client: httpx.Client | None = None,
    ) -> None:
        self._name = name
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._timeout_seconds = timeout_seconds
        self._client = client or httpx.Client(timeout=timeout_seconds)

    @property
    def name(self) -> str:
        return self._name

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }

    @staticmethod
    def _parse_rate_limit_reset(response: httpx.Response) -> str | None:
        reset_raw = response.headers.get("X-RateLimit-Reset")
        if not reset_raw:
            return None
        try:
            reset_ms = int(reset_raw)
        except ValueError:
            return None
        return datetime.fromtimestamp(reset_ms / 1000, tz=UTC).isoformat()

    def _to_app_error(self, exc: httpx.HTTPStatusError) -> AppError:
        response = exc.response
        status = response.status_code
        body_text = response.text

        if status == 429:
            reset_at = self._parse_rate_limit_reset(response)
            suffix = f" reset_at={reset_at}" if reset_at else ""
            return AppError(
                "provider_rate_limit",
                f"Rate limit exceeded (429){suffix}. body={body_text}",
                429,
            )

        if status in {401, 403}:
            return AppError("authentication_error", f"OpenAI auth error: {body_text}", status)

        if status >= 500:
            return AppError("provider_execution_error", f"OpenAI server error: {body_text}", 502)

        return AppError("invalid_request", f"OpenAI error: {body_text}", 400)

    def list_models(self) -> list[str]:
        url = f"{self._base_url}/models"
        try:
            response = self._client.get(url, headers=self._headers())
            response.raise_for_status()
            payload = response.json()
            models = payload.get("data", [])
            return [item.get("id", "") for item in models if item.get("id")]
        except httpx.TimeoutException as exc:
            raise TimeoutError("OpenAI model discovery timed out") from exc
        except httpx.HTTPStatusError as exc:
            raise self._to_app_error(exc) from exc
        except httpx.HTTPError as exc:
            raise ConnectionError("OpenAI model discovery connection error") from exc

    def health_check(self) -> bool:
        return len(self.list_models()) >= 0

    def execute_prompt(self, request: ProviderRequest) -> ProviderResponse:
        url = f"{self._base_url}/chat/completions"
        body = {
            "model": request.model_name,
            "messages": [
                {"role": "system", "content": request.system_prompt},
                {"role": "developer", "content": request.developer_prompt},
                {"role": "user", "content": request.user_prompt},
            ],
            "temperature": 0,
        }

        start = perf_counter()
        try:
            response = self._client.post(url, headers=self._headers(), json=body)
            response.raise_for_status()
            payload = response.json()
            choice = payload["choices"][0]
            usage = payload.get("usage", {})
            content = choice["message"]["content"]
            finish_reason = choice.get("finish_reason", "stop")
            latency_ms = int((perf_counter() - start) * 1000)
            return ProviderResponse(
                provider_name=self.name,
                model_name=request.model_name,
                model_version=payload.get("model", request.model_name),
                content=content,
                input_tokens=int(usage.get("prompt_tokens", 0)),
                output_tokens=int(usage.get("completion_tokens", 0)),
                finish_reason=finish_reason,
                latency_ms=latency_ms,
            )
        except httpx.TimeoutException as exc:
            raise TimeoutError("OpenAI completion timed out") from exc
        except httpx.HTTPStatusError as exc:
            raise self._to_app_error(exc) from exc
        except httpx.HTTPError as exc:
            raise ConnectionError("OpenAI completion connection error") from exc
