from pathlib import Path
import sys
import argparse
import json
import re

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.application.benchmarking.benchmark_engine import BenchmarkEngine
from app.application.benchmarking.models import (
    BenchmarkDefinition,
    BenchmarkQuestion,
    PromptTemplate,
)
from app.application.benchmarking.scoring_engine import ScoringEngine
from app.application.benchmarking.trial_service import BenchmarkTrialService
from app.application.providers.provider_manager import ProviderManager
from app.application.providers.provider_registry import ProviderRegistry
from app.application.providers.provider_bootstrap import create_provider_manager
from app.infrastructure.config.settings import get_settings
from app.infrastructure.providers.mock_provider_adapter import MockProviderAdapter


def _resolve_dataset_file(dataset_file: str | None) -> Path:
    if dataset_file is None:
        return Path(__file__).resolve().parents[1] / "datasets" / "counselor_skill_assessment_v2.json"
    return Path(dataset_file)


def _infer_dataset_meta(dataset_file: Path) -> tuple[str, str]:
    stem = dataset_file.stem
    match = re.search(r"_v(\d+)$", stem)
    if match:
        version = f"v{match.group(1)}"
        name = stem[: match.start()]
        return name, version
    return stem, "v1"


def _load_questions(dataset_file: Path) -> list[BenchmarkQuestion]:
    payload = json.loads(dataset_file.read_text(encoding="utf-8"))
    questions: list[BenchmarkQuestion] = []
    for item in payload:
        questions.append(
            BenchmarkQuestion(
                id=str(item["id"]),
                prompt=str(item["prompt"]),
                expected_answer=str(item["expected_answer"]),
                evaluation_type=str(item.get("evaluation_type", "exact_match")),
                categories=[str(category) for category in item.get("categories", ["accuracy"])],
                accepted_answers=[str(answer) for answer in item.get("accepted_answers", [])],
                expected_keywords=[str(keyword) for keyword in item.get("expected_keywords", [])],
            )
        )
    return questions


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run benchmark trial")
    parser.add_argument("--provider", choices=["mock", "openai"], default=None)
    parser.add_argument("--model", default=None)
    parser.add_argument("--dataset-file", default=None)
    parser.add_argument("--pass-threshold", type=float, default=0.8)
    parser.add_argument("--report-file", default="benchmark_trial_report.json")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    settings = get_settings()
    provider_name = args.provider or ("openai" if settings.openai_api_key else "mock")
    model_name = args.model or (
        settings.openai_model_name if provider_name == "openai" else "mock-model-v1"
    )
    dataset_file = _resolve_dataset_file(args.dataset_file)
    dataset_name, dataset_version = _infer_dataset_meta(dataset_file)
    questions = _load_questions(dataset_file)

    if provider_name == "mock":
        # Deterministic smoke test behavior for local benchmark validation.
        registry = ProviderRegistry()
        scripted_outputs = {}
        for question in questions:
            if question.evaluation_type == "keyword":
                scripted_outputs[question.prompt] = " ".join(question.expected_keywords)
            else:
                scripted_outputs[question.prompt] = question.expected_answer or ""
        registry.register(
            MockProviderAdapter(
                name="mock",
                scripted_outputs=scripted_outputs,
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
        benchmark_id=f"benchmark-{dataset_name}",
        benchmark_version="1.2.0",
        provider_name=provider_name,
        model_name=model_name,
        model_version="runtime",
        dataset_name=dataset_name,
        dataset_version=dataset_version,
        questions=questions,
        prompt_template=PromptTemplate(
            version="v1",
            system_prompt="You are an accurate evaluator.",
            developer_prompt="Answer briefly.",
            user_template="{question}",
        ),
    )

    result = engine.run(definition)
    trial_service = BenchmarkTrialService(pass_threshold=args.pass_threshold)
    report = trial_service.build_report(result)
    trial_service.save_report(report, args.report_file)

    print("provider:", result.provider_name)
    print("model:", result.model_name)
    print("overall_score:", result.score.overall_score)
    print("pass_threshold:", report.pass_threshold)
    print("passed:", report.passed)
    print("report_file:", args.report_file)
    for item in result.responses:
        print(item.question_id, "=>", item.answer, "(expected:", item.expected_answer + ")")

    if not report.passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
