from app.application.providers.interfaces import (
    ProviderAdapter,
    ProviderRequest,
    ProviderResponse,
)


class MockProviderAdapter(ProviderAdapter):
    def __init__(
        self,
        *,
        name: str = "mock",
        model_name: str = "mock-model-v1",
        model_version: str = "v1",
        scripted_outputs: dict[str, str] | None = None,
    ) -> None:
        self._name = name
        self._model_name = model_name
        self._model_version = model_version
        self._scripted_outputs = scripted_outputs or {}

    @property
    def name(self) -> str:
        return self._name

    def list_models(self) -> list[str]:
        return [self._model_name]

    def health_check(self) -> bool:
        return True

    def execute_prompt(self, request: ProviderRequest) -> ProviderResponse:
        content = self._scripted_outputs.get(request.user_prompt, "I am here with you.")
        input_tokens = max(1, len(request.user_prompt.split()))
        output_tokens = max(1, len(content.split()))
        return ProviderResponse(
            provider_name=self._name,
            model_name=request.model_name,
            model_version=self._model_version,
            content=content,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            finish_reason="stop",
            latency_ms=1,
        )
