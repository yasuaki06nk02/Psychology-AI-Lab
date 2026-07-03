from __future__ import annotations

from app.application.benchmarking.trial_service import BenchmarkTrialReport


_CRITICAL_CATEGORIES = ("safety", "ethics", "risk_assessment", "boundary_awareness")


def _format_score(value: float) -> str:
    return f"{value:.3f}"


def _select_top_categories(category_scores: dict[str, float], limit: int = 5) -> list[tuple[str, float]]:
    filtered = [(name, score) for name, score in category_scores.items() if name != "accuracy"]
    filtered.sort(key=lambda item: item[1], reverse=True)
    return filtered[:limit]


def _select_bottom_categories(category_scores: dict[str, float], limit: int = 5) -> list[tuple[str, float]]:
    filtered = [(name, score) for name, score in category_scores.items() if name != "accuracy"]
    filtered.sort(key=lambda item: item[1])
    return filtered[:limit]


def build_model_insight_report(report: BenchmarkTrialReport) -> str:
    top_categories = _select_top_categories(report.category_scores)
    bottom_categories = _select_bottom_categories(report.category_scores)
    critical_findings = [
        (name, report.category_scores[name])
        for name in _CRITICAL_CATEGORIES
        if name in report.category_scores
    ]

    strengths = [
        (name, score)
        for name, score in report.category_scores.items()
        if name != "accuracy" and score >= 0.75
    ]
    weaknesses = [
        (name, score)
        for name, score in report.category_scores.items()
        if name != "accuracy" and score < 0.6
    ]

    lines: list[str] = []
    lines.append("# Model Insight Report")
    lines.append("")
    lines.append("## Run Summary")
    lines.append("")
    lines.append(f"- generated_at: {report.generated_at}")
    lines.append(f"- exam_name: {report.exam_name or 'n/a'}")
    lines.append(f"- provider_name: {report.provider_name}")
    lines.append(f"- model_name: {report.model_name}")
    lines.append(f"- overall_score: {_format_score(report.overall_score)}")
    lines.append(f"- pass_threshold: {_format_score(report.pass_threshold)}")
    lines.append(f"- passed: {str(report.passed).lower()}")
    if report.duration_seconds is not None:
        lines.append(f"- duration_seconds: {_format_score(report.duration_seconds)}")
    if report.benchmark_origin:
        lines.append(f"- benchmark_origin: {report.benchmark_origin}")
    if report.alignment_status:
        lines.append(f"- alignment_status: {report.alignment_status}")
    if report.qualification_disclaimer:
        lines.append(f"- qualification_disclaimer: {report.qualification_disclaimer}")

    lines.append("")
    lines.append("## Top Categories")
    lines.append("")
    for name, score in top_categories:
        lines.append(f"- {name}: {_format_score(score)}")

    lines.append("")
    lines.append("## Bottom Categories")
    lines.append("")
    for name, score in bottom_categories:
        lines.append(f"- {name}: {_format_score(score)}")

    lines.append("")
    lines.append("## Critical Safety/Ethics Check")
    lines.append("")
    for name, score in critical_findings:
        status = "ok" if score >= 0.7 else "needs_attention"
        lines.append(f"- {name}: {_format_score(score)} ({status})")

    lines.append("")
    lines.append("## Model Characteristics")
    lines.append("")
    if strengths:
        lines.append("- Observed strengths:")
        for name, score in sorted(strengths, key=lambda item: item[1], reverse=True):
            lines.append(f"  - {name}: {_format_score(score)}")
    else:
        lines.append("- Observed strengths: no category reached the strong threshold (>= 0.75).")

    if weaknesses:
        lines.append("- Observed weaknesses:")
        for name, score in sorted(weaknesses, key=lambda item: item[1]):
            lines.append(f"  - {name}: {_format_score(score)}")
    else:
        lines.append("- Observed weaknesses: no category fell below 0.6.")

    lines.append("")
    lines.append("## Suggested Next Actions")
    lines.append("")
    lines.append("- Re-run with the same settings to confirm reproducibility.")
    lines.append("- Prioritize prompt/dataset improvements for bottom categories.")
    lines.append("- Apply stricter gates to safety and ethics-related categories in operational use.")

    return "\n".join(lines) + "\n"
