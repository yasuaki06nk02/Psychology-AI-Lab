from pathlib import Path
import sys
import argparse
import json
import re
from time import perf_counter

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.application.benchmarking.benchmark_engine import BenchmarkEngine
from app.application.benchmarking.models import (
    BenchmarkDefinition,
    BenchmarkQuestion,
    PromptTemplate,
)
from app.application.benchmarking.scoring_engine import ScoringEngine
from app.application.benchmarking.insight_report import build_model_insight_report
from app.application.benchmarking.trial_service import BenchmarkTrialService
from app.application.errors import AppError
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


def _infer_exam_name(dataset_name: str) -> str:
    mapping = {
        "counselor_skill_assessment": "Counselor Skill Assessment (Public + Clinical)",
        "psychology_eval": "Psychology Evaluation Trial",
    }
    return mapping.get(dataset_name, dataset_name.replace("_", " ").title())


def _load_dataset(dataset_file: Path) -> tuple[list[BenchmarkQuestion], dict[str, object]]:
    payload = json.loads(dataset_file.read_text(encoding="utf-8"))
    items = payload
    metadata: dict[str, object] = {}

    if isinstance(payload, dict):
        metadata = payload.get("metadata", {}) if isinstance(payload.get("metadata", {}), dict) else {}
        items = payload.get("questions", [])

    questions: list[BenchmarkQuestion] = []
    for item in items:
        questions.append(
            BenchmarkQuestion(
                id=str(item["id"]),
                prompt=str(item["prompt"]),
                expected_answer=str(item["expected_answer"]),
                evaluation_type=str(item.get("evaluation_type", "exact_match")),
                categories=[str(category) for category in item.get("categories", ["accuracy"])],
                accepted_answers=[str(answer) for answer in item.get("accepted_answers", [])],
                expected_keywords=[str(keyword) for keyword in item.get("expected_keywords", [])],
                expected_reference=str(item.get("expected_reference", "")),
            )
        )
    return questions, metadata


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run benchmark trial")
    parser.add_argument("--provider", choices=["mock", "openai", "gemini"], default=None)
    parser.add_argument("--model", default=None)
    parser.add_argument("--dataset-file", default=None)
    parser.add_argument("--pass-threshold", type=float, default=0.8)
    parser.add_argument("--report-file", default="benchmark_trial_report.json")
    parser.add_argument("--insight-report-file", default=None)
    parser.add_argument("--inter-request-delay-seconds", type=float, default=0.0)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    settings = get_settings()
    if args.provider:
        provider_name = args.provider
    elif settings.openai_api_key:
        provider_name = "openai"
    elif settings.gemini_api_key:
        provider_name = "gemini"
    else:
        provider_name = "mock"

    if args.model:
        model_name = args.model
    elif provider_name == "openai":
        model_name = settings.openai_model_name
    elif provider_name == "gemini":
        model_name = settings.gemini_model_name
    else:
        model_name = "mock-model-v1"
    dataset_file = _resolve_dataset_file(args.dataset_file)
    dataset_name, dataset_version = _infer_dataset_meta(dataset_file)
    questions, dataset_metadata = _load_dataset(dataset_file)
    exam_name = str(dataset_metadata.get("exam_name") or _infer_exam_name(dataset_name))
    benchmark_origin = str(dataset_metadata.get("benchmark_origin")) if dataset_metadata.get("benchmark_origin") else None
    alignment_status = str(dataset_metadata.get("alignment_status")) if dataset_metadata.get("alignment_status") else None
    qualification_equivalence_raw = dataset_metadata.get("qualification_equivalence")
    qualification_equivalence = (
        bool(qualification_equivalence_raw)
        if isinstance(qualification_equivalence_raw, bool)
        else None
    )
    qualification_disclaimer = (
        str(dataset_metadata.get("qualification_disclaimer"))
        if dataset_metadata.get("qualification_disclaimer")
        else None
    )
    source_references_raw = dataset_metadata.get("source_references")
    source_references = (
        [str(item) for item in source_references_raw]
        if isinstance(source_references_raw, list)
        else []
    )

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
        inter_request_delay_seconds=max(0.0, args.inter_request_delay_seconds),
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

    run_started_at = perf_counter()

    def _progress(status: str, index: int, total: int, question_id: str, elapsed_seconds: float) -> None:
        if status == "started":
            print(f"[progress] {index}/{total} {question_id} started", flush=True)
            return
        if status == "completed":
            print(
                f"[progress] {index}/{total} {question_id} completed in {elapsed_seconds:.2f}s",
                flush=True,
            )
            return
        print(
            f"[progress] {index}/{total} {question_id} failed after {elapsed_seconds:.2f}s",
            flush=True,
        )

    try:
        result = engine.run_with_progress(definition, progress_callback=_progress)
    except AppError as exc:
        duration_seconds = perf_counter() - run_started_at
        print("benchmark_failed:", exc.code, flush=True)
        print("error_message:", exc.message, flush=True)
        print("duration_seconds:", f"{duration_seconds:.2f}", flush=True)
        if exc.code == "provider_rate_limit":
            if provider_name == "gemini":
                print(
                    "hint: Gemini free tier rate limit reached. Try --inter-request-delay-seconds 12 (or more), wait for retry window, or upgrade quota.",
                    flush=True,
                )
            elif provider_name == "openai":
                print("hint: OpenRouter/OpenAI rate limit reached. Retry after reset or add credits.", flush=True)
            else:
                print("hint: Provider rate limit reached. Retry later or reduce request speed.", flush=True)
        raise SystemExit(1)

    duration_seconds = perf_counter() - run_started_at
    trial_service = BenchmarkTrialService(pass_threshold=args.pass_threshold)
    report = trial_service.build_report(
        result,
        duration_seconds=duration_seconds,
        exam_name=exam_name,
        benchmark_origin=benchmark_origin,
        alignment_status=alignment_status,
        qualification_equivalence=qualification_equivalence,
        qualification_disclaimer=qualification_disclaimer,
        source_references=source_references,
    )
    trial_service.save_report(report, args.report_file)

    insight_file = args.insight_report_file
    if not insight_file:
        report_path = Path(args.report_file)
        insight_file = str(report_path.with_name(report_path.stem + "_insight.md"))

    insight_text = build_model_insight_report(report)
    insight_path = Path(insight_file)
    insight_path.parent.mkdir(parents=True, exist_ok=True)
    insight_path.write_text(insight_text, encoding="utf-8")

    print("exam_name:", exam_name)
    if benchmark_origin:
        print("benchmark_origin:", benchmark_origin)
    if alignment_status:
        print("alignment_status:", alignment_status)
    if qualification_disclaimer:
        print("qualification_disclaimer:", qualification_disclaimer)
    print("provider:", result.provider_name)
    print("model:", result.model_name)
    print("overall_score:", result.score.overall_score)
    print("pass_threshold:", report.pass_threshold)
    print("passed:", report.passed)
    print("duration_seconds:", f"{duration_seconds:.2f}")
    print("report_file:", args.report_file)
    print("insight_report_file:", insight_file)
    for item in result.responses:
        if item.evaluation_type == "keyword":
            expected_display = item.expected_reference or ("keywords: " + ", ".join(item.expected_keywords))
        else:
            expected_display = item.expected_answer
        print(item.question_id, "=>", item.answer, "(expected:", expected_display + ")")

    if not report.passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
