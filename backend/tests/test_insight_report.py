from app.application.benchmarking.insight_report import build_model_insight_report
from app.application.benchmarking.trial_service import BenchmarkTrialReport


def test_build_model_insight_report_contains_core_sections() -> None:
    report = BenchmarkTrialReport(
        generated_at="2026-07-04T00:00:00+00:00",
        exam_name="2026年 テスト試験",
        benchmark_origin="custom_internal_benchmark",
        alignment_status="partial_alignment",
        qualification_equivalence=False,
        qualification_disclaimer="not equivalent to qualification",
        source_references=["ref-a", "ref-b"],
        provider_name="gemini",
        model_name="gemini-2.5-flash",
        benchmark_id="b1",
        benchmark_version="1.0.0",
        dataset_name="ds",
        dataset_version="v1",
        prompt_version="v1",
        overall_score=0.66,
        category_scores={
            "accuracy": 0.66,
            "safety": 0.5,
            "ethics": 0.8,
            "act": 0.3,
            "knowledge": 1.0,
        },
        duration_seconds=120.0,
        pass_threshold=0.8,
        passed=False,
    )

    text = build_model_insight_report(report)

    assert "# Model Insight Report" in text
    assert "## Run Summary" in text
    assert "## Top Categories" in text
    assert "## Bottom Categories" in text
    assert "## Critical Safety/Ethics Check" in text
    assert "## Model Characteristics" in text
    assert "## Suggested Next Actions" in text
    assert "- passed: false" in text
    assert "- safety: 0.500 (needs_attention)" in text
