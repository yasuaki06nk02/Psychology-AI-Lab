from time import sleep
from time import perf_counter
from typing import Callable

from app.application.errors import AppError
from app.application.benchmarking.models import (
    BenchmarkDefinition,
    BenchmarkResponse,
    BenchmarkRunResult,
)
from app.application.benchmarking.scoring_engine import ScoringEngine
from app.application.providers.interfaces import ProviderRequest
from app.application.providers.provider_manager import ProviderManager


class BenchmarkEngine:
    def __init__(
        self,
        provider_manager: ProviderManager,
        scoring_engine: ScoringEngine,
        *,
        max_retries: int = 0,
        retry_delay_seconds: float = 0.0,
    ) -> None:
        self._provider_manager = provider_manager
        self._scoring_engine = scoring_engine
        self._max_retries = max_retries
        self._retry_delay_seconds = retry_delay_seconds

    def run(self, definition: BenchmarkDefinition) -> BenchmarkRunResult:
        return self.run_with_progress(definition)

    def run_with_progress(
        self,
        definition: BenchmarkDefinition,
        progress_callback: Callable[[str, int, int, str, float], None] | None = None,
    ) -> BenchmarkRunResult:
        responses: list[BenchmarkResponse] = []
        run_started_at = perf_counter()
        total_questions = len(definition.questions)

        for index, question in enumerate(definition.questions, start=1):
            question_started_at = perf_counter()
            if progress_callback is not None:
                progress_callback(
                    "started",
                    index,
                    total_questions,
                    question.id,
                    question_started_at - run_started_at,
                )

            user_prompt = definition.prompt_template.user_template.format(
                question=question.prompt,
                question_id=question.id,
            )

            request = ProviderRequest(
                model_name=definition.model_name,
                system_prompt=definition.prompt_template.system_prompt,
                developer_prompt=definition.prompt_template.developer_prompt,
                user_prompt=user_prompt,
            )
            try:
                provider_response = self._execute_with_retry(definition.provider_name, request)
            except Exception:
                if progress_callback is not None:
                    progress_callback(
                        "failed",
                        index,
                        total_questions,
                        question.id,
                        perf_counter() - question_started_at,
                    )
                raise

            responses.append(
                BenchmarkResponse(
                    question_id=question.id,
                    prompt=user_prompt,
                    answer=provider_response.content,
                    expected_answer=question.expected_answer,
                    evaluation_type=question.evaluation_type,
                    categories=question.categories,
                    accepted_answers=question.accepted_answers,
                    expected_keywords=question.expected_keywords,
                    latency_ms=provider_response.latency_ms,
                    input_tokens=provider_response.input_tokens,
                    output_tokens=provider_response.output_tokens,
                )
            )

            if progress_callback is not None:
                progress_callback(
                    "completed",
                    index,
                    total_questions,
                    question.id,
                    perf_counter() - question_started_at,
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

    def _execute_with_retry(
        self,
        provider_name: str,
        request: ProviderRequest,
    ):
        attempts = self._max_retries + 1
        last_error: AppError | None = None
        retryable_codes = {
            "provider_timeout",
            "provider_connection_error",
            "provider_execution_error",
        }

        for attempt in range(attempts):
            try:
                return self._provider_manager.execute_prompt(provider_name, request)
            except AppError as exc:
                last_error = exc
                should_retry = exc.code in retryable_codes and attempt < attempts - 1
                if not should_retry:
                    raise
                if self._retry_delay_seconds > 0:
                    sleep(self._retry_delay_seconds)

        if last_error is not None:
            raise last_error
        raise AppError("provider_execution_error", "Provider execution failed", 502)
