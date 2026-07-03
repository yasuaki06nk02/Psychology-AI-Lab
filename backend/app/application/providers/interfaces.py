from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True, slots=True)
class ProviderRequest:
    model_name: str
    system_prompt: str
    developer_prompt: str
    user_prompt: str


@dataclass(frozen=True, slots=True)
class ProviderResponse:
    provider_name: str
    model_name: str
    model_version: str
    content: str
    input_tokens: int
    output_tokens: int
    finish_reason: str
    latency_ms: int


class ProviderAdapter(Protocol):
    @property
    def name(self) -> str: ...

    def list_models(self) -> list[str]: ...

    def health_check(self) -> bool: ...

    def execute_prompt(self, request: ProviderRequest) -> ProviderResponse: ...
