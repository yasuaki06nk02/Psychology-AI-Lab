from app.application.benchmarking.benchmark_engine import BenchmarkEngine
from app.application.benchmarking.models import (
    BenchmarkDefinition,
    BenchmarkQuestion,
    PromptTemplate,
)
from app.application.benchmarking.scoring_engine import ScoringEngine
from app.application.providers.provider_manager import ProviderManager
from app.application.providers.provider_registry import ProviderRegistry
from app.infrastructure.providers.mock_provider_adapter import MockProviderAdapter


def _create_definition() -> BenchmarkDefinition:
    questions = [
        BenchmarkQuestion(id="q1", prompt="2+2?", expected_answer="4"),
        BenchmarkQuestion(id="q2", prompt="3+5?", expected_answer="8"),
    ]

    template = PromptTemplate(
        version="v1",
        system_prompt="You are an evaluator.",
        developer_prompt="Answer with number only.",
        user_template="QID:{question_id} QUESTION:{question}",
    )

    return BenchmarkDefinition(
        benchmark_id="bench-1",
        benchmark_version="1.0.0",
        provider_name="mock",
        model_name="mock-model-v1",
        model_version="v1",
        dataset_name="math-mini",
        dataset_version="v1",
        questions=questions,
        prompt_template=template,
    )


def _create_engine() -> BenchmarkEngine:
    scripted_outputs = {
        "QID:q1 QUESTION:2+2?": "4",
        "QID:q2 QUESTION:3+5?": "8",
    }
    registry = ProviderRegistry()
    registry.register(MockProviderAdapter(name="mock", scripted_outputs=scripted_outputs))
    manager = ProviderManager(registry)
    return BenchmarkEngine(manager, ScoringEngine())


def test_benchmark_run_is_reproducible() -> None:
    definition = _create_definition()
    engine = _create_engine()

    first = engine.run(definition)
    second = engine.run(definition)

    assert first.responses == second.responses
    assert first.score == second.score
    assert first.score.overall_score == 1.0


def test_benchmark_score_is_consistent_for_partial_correct_answers() -> None:
    definition = _create_definition()

    scripted_outputs = {
        "QID:q1 QUESTION:2+2?": "4",
        "QID:q2 QUESTION:3+5?": "7",
    }
    registry = ProviderRegistry()
    registry.register(MockProviderAdapter(name="mock", scripted_outputs=scripted_outputs))
    engine = BenchmarkEngine(ProviderManager(registry), ScoringEngine())

    result = engine.run(definition)

    assert result.score.category_scores["accuracy"] == 0.5
    assert result.score.overall_score == 0.5
