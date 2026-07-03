from __future__ import annotations

from datetime import UTC, datetime
from time import perf_counter
from urllib.parse import urlencode

import httpx

from app.application.errors import AppError
from app.application.providers.interfaces import (
    ProviderAdapter,
    ProviderRequest,
    ProviderResponse,
)


class GeminiProviderAdapter(ProviderAdapter):
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str,
        timeout_seconds: float,
        client: httpx.Client | None = None,
    ) -> None:
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._timeout_seconds = timeout_seconds
        self._client = client or httpx.Client(timeout=timeout_seconds)

    @property
    def name(self) -> str:
        return "gemini"

    def _build_url(self, path: str) -> str:
        query = urlencode({"key": self._api_key})
        return f"{self._base_url}/{path}?{query}"

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
                f"Gemini rate limit exceeded (429){suffix}. body={body_text}",
                429,
            )

        if status in {401, 403}:
            return AppError("authentication_error", f"Gemini auth error: {body_text}", status)

        if status >= 500:
            return AppError("provider_execution_error", f"Gemini server error: {body_text}", 502)

        return AppError("invalid_request", f"Gemini error: {body_text}", 400)

    def list_models(self) -> list[str]:
        url = self._build_url("models")
        try:
            response = self._client.get(url)
            response.raise_for_status()
            payload = response.json()
            models = payload.get("models", [])
            names: list[str] = []
            for item in models:
                raw_name = str(item.get("name", ""))
                if raw_name.startswith("models/"):
                    names.append(raw_name.split("/", 1)[1])
                elif raw_name:
                    names.append(raw_name)
            return names
        except httpx.TimeoutException as exc:
            raise TimeoutError("Gemini model discovery timed out") from exc
        except httpx.HTTPStatusError as exc:
            raise self._to_app_error(exc) from exc
        except httpx.HTTPError as exc:
            raise ConnectionError("Gemini model discovery connection error") from exc

    def health_check(self) -> bool:
        return len(self.list_models()) >= 0

    def execute_prompt(self, request: ProviderRequest) -> ProviderResponse:
        url = self._build_url(f"models/{request.model_name}:generateContent")
        body = {
            "systemInstruction": {
                "parts": [{"text": request.system_prompt}],
            },
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": (
                                f"Developer instructions:\n{request.developer_prompt}\n\n"
                                f"User question:\n{request.user_prompt}"
                            )
                        }
                    ],
                }
            ],
            "generationConfig": {"temperature": 0},
        }

        start = perf_counter()
        try:
            response = self._client.post(url, json=body)
            response.raise_for_status()
            payload = response.json()
            candidate = payload["candidates"][0]
            parts = candidate.get("content", {}).get("parts", [])
            content = "\n".join(str(part.get("text", "")) for part in parts).strip()
            usage = payload.get("usageMetadata", {})
            latency_ms = int((perf_counter() - start) * 1000)
            return ProviderResponse(
                provider_name=self.name,
                model_name=request.model_name,
                model_version=request.model_name,
                content=content,
                input_tokens=int(usage.get("promptTokenCount", 0)),
                output_tokens=int(usage.get("candidatesTokenCount", 0)),
                finish_reason=str(candidate.get("finishReason", "STOP")),
                latency_ms=latency_ms,
            )
        except httpx.TimeoutException as exc:
            raise TimeoutError("Gemini completion timed out") from exc
        except httpx.HTTPStatusError as exc:
            raise self._to_app_error(exc) from exc
        except httpx.HTTPError as exc:
            raise ConnectionError("Gemini completion connection error") from exc
