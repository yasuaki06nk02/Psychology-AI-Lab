from app.application.benchmarking.benchmark_engine import BenchmarkEngine
from app.application.benchmarking.models import (
    BenchmarkDefinition,
    BenchmarkQuestion,
    PromptTemplate,
)
from app.application.benchmarking.scoring_engine import ScoringEngine
from app.application.providers.interfaces import ProviderAdapter, ProviderRequest, ProviderResponse
from app.application.providers.provider_manager import ProviderManager
from app.application.providers.provider_registry import ProviderRegistry


class FlakyAdapter(ProviderAdapter):
    def __init__(self) -> None:
        self._calls = 0

    @property
    def name(self) -> str:
        return "flaky"

    def list_models(self) -> list[str]:
        return ["flaky-model"]

    def health_check(self) -> bool:
        return True

    def execute_prompt(self, request: ProviderRequest) -> ProviderResponse:
        self._calls += 1
        if self._calls == 1:
            raise TimeoutError("temporary timeout")
        return ProviderResponse(
            provider_name="flaky",
            model_name=request.model_name,
            model_version="v1",
            content="4",
            input_tokens=1,
            output_tokens=1,
            finish_reason="stop",
            latency_ms=1,
        )


def test_benchmark_engine_retries_transient_error() -> None:
    registry = ProviderRegistry()
    registry.register(FlakyAdapter())
    engine = BenchmarkEngine(
        ProviderManager(registry),
        ScoringEngine(),
        max_retries=1,
        retry_delay_seconds=0,
    )

    result = engine.run(
        BenchmarkDefinition(
            benchmark_id="b1",
            benchmark_version="1",
            provider_name="flaky",
            model_name="flaky-model",
            model_version="v1",
            dataset_name="ds",
            dataset_version="v1",
            questions=[BenchmarkQuestion(id="q1", prompt="2+2?", expected_answer="4")],
            prompt_template=PromptTemplate(
                version="v1",
                system_prompt="s",
                developer_prompt="d",
                user_template="{question}",
            ),
        )
    )

    assert result.score.overall_score == 1.0
