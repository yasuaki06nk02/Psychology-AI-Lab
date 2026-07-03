from app.application.benchmarking.models import (
    BenchmarkDefinition,
    BenchmarkResponse,
    BenchmarkRunResult,
)
from app.application.benchmarking.scoring_engine import ScoringEngine
from app.application.providers.interfaces import ProviderRequest
from app.application.providers.provider_manager import ProviderManager


class BenchmarkEngine:
    def __init__(self, provider_manager: ProviderManager, scoring_engine: ScoringEngine) -> None:
        self._provider_manager = provider_manager
        self._scoring_engine = scoring_engine

    def run(self, definition: BenchmarkDefinition) -> BenchmarkRunResult:
        responses: list[BenchmarkResponse] = []

        for question in definition.questions:
            user_prompt = definition.prompt_template.user_template.format(
                question=question.prompt,
                question_id=question.id,
            )

            provider_response = self._provider_manager.execute_prompt(
                definition.provider_name,
                ProviderRequest(
                    model_name=definition.model_name,
                    system_prompt=definition.prompt_template.system_prompt,
                    developer_prompt=definition.prompt_template.developer_prompt,
                    user_prompt=user_prompt,
                ),
            )

            responses.append(
                BenchmarkResponse(
                    question_id=question.id,
                    prompt=user_prompt,
                    answer=provider_response.content,
                    expected_answer=question.expected_answer,
                    latency_ms=provider_response.latency_ms,
                    input_tokens=provider_response.input_tokens,
                    output_tokens=provider_response.output_tokens,
                )
            )

        score = self._scoring_engine.score(responses)

        return BenchmarkRunResult(
            benchmark_id=definition.benchmark_id,
            benchmark_version=definition.benchmark_version,
            dataset_name=definition.dataset_name,
            dataset_version=definition.dataset_version,
            provider_name=definition.provider_name,
            model_name=definition.model_name,
            model_version=definition.model_version,
            prompt_version=definition.prompt_template.version,
            responses=responses,
            score=score,
        )
