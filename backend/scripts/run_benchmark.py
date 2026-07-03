from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.application.benchmarking.benchmark_engine import BenchmarkEngine
from app.application.benchmarking.models import (
    BenchmarkDefinition,
    BenchmarkQuestion,
    PromptTemplate,
)
from app.application.benchmarking.scoring_engine import ScoringEngine
from app.application.providers.provider_manager import ProviderManager
from app.application.providers.provider_registry import ProviderRegistry
from app.application.providers.provider_bootstrap import create_provider_manager
from app.infrastructure.config.settings import get_settings
from app.infrastructure.providers.mock_provider_adapter import MockProviderAdapter


def main() -> None:
    settings = get_settings()
    provider_name = "openai" if settings.openai_api_key else "mock"

    if provider_name == "mock":
        # Deterministic smoke test behavior for local benchmark validation.
        registry = ProviderRegistry()
        registry.register(
            MockProviderAdapter(
                name="mock",
                scripted_outputs={
                    "2+2?": "4",
                    "3+5?": "8",
                },
            )
        )
        manager = ProviderManager(registry)
    else:
        manager = create_provider_manager(settings)
    engine = BenchmarkEngine(
        manager,
        ScoringEngine(),
        max_retries=settings.provider_max_retries,
        retry_delay_seconds=settings.provider_retry_delay_seconds,
    )

    definition = BenchmarkDefinition(
        benchmark_id="benchmark-operational-smoke",
        benchmark_version="1.0.0",
        provider_name=provider_name,
        model_name="gpt-4o-mini" if provider_name == "openai" else "mock-model-v1",
        model_version="runtime",
        dataset_name="smoke-dataset",
        dataset_version="v1",
        questions=[
            BenchmarkQuestion(id="q1", prompt="2+2?", expected_answer="4"),
            BenchmarkQuestion(id="q2", prompt="3+5?", expected_answer="8"),
        ],
        prompt_template=PromptTemplate(
            version="v1",
            system_prompt="You are an accurate evaluator.",
            developer_prompt="Answer briefly.",
            user_template="{question}",
        ),
    )

    result = engine.run(definition)
    print("provider:", result.provider_name)
    print("model:", result.model_name)
    print("overall_score:", result.score.overall_score)
    for item in result.responses:
        print(item.question_id, "=>", item.answer, "(expected:", item.expected_answer + ")")


if __name__ == "__main__":
    main()
