from app.application.benchmarking.models import BenchmarkResponse, BenchmarkRunResult, ScoreResult
from app.application.benchmarking.trial_service import BenchmarkTrialService


def _result(score: float) -> BenchmarkRunResult:
    return BenchmarkRunResult(
        benchmark_id="b1",
        benchmark_version="1.0.0",
        dataset_name="dataset",
        dataset_version="v1",
        provider_name="mock",
        model_name="mock-model-v1",
        model_version="runtime",
        prompt_version="v1",
        responses=[
            BenchmarkResponse(
                question_id="q1",
                prompt="2+2?",
                answer="4",
                expected_answer="4",
                latency_ms=1,
                input_tokens=1,
                output_tokens=1,
            )
        ],
        score=ScoreResult(category_scores={"accuracy": score}, overall_score=score),
    )


def test_trial_report_passes_when_score_meets_threshold() -> None:
    service = BenchmarkTrialService(pass_threshold=0.8)
    report = service.build_report(_result(0.9))

    assert report.passed is True
    assert report.overall_score == 0.9


def test_trial_report_fails_when_score_below_threshold() -> None:
    service = BenchmarkTrialService(pass_threshold=0.8)
    report = service.build_report(_result(0.5))

    assert report.passed is False
    assert report.pass_threshold == 0.8
