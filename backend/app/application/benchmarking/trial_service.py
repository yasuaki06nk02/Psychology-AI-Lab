from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path

from app.application.benchmarking.models import BenchmarkRunResult


@dataclass(frozen=True, slots=True)
class BenchmarkTrialReport:
    generated_at: str
    provider_name: str
    model_name: str
    benchmark_id: str
    benchmark_version: str
    dataset_name: str
    dataset_version: str
    prompt_version: str
    overall_score: float
    category_scores: dict[str, float]
    pass_threshold: float
    passed: bool


class BenchmarkTrialService:
    def __init__(self, pass_threshold: float) -> None:
        self._pass_threshold = pass_threshold

    def build_report(self, result: BenchmarkRunResult) -> BenchmarkTrialReport:
        overall_score = result.score.overall_score
        return BenchmarkTrialReport(
            generated_at=datetime.now(UTC).isoformat(),
            provider_name=result.provider_name,
            model_name=result.model_name,
            benchmark_id=result.benchmark_id,
            benchmark_version=result.benchmark_version,
            dataset_name=result.dataset_name,
            dataset_version=result.dataset_version,
            prompt_version=result.prompt_version,
            overall_score=overall_score,
            category_scores=result.score.category_scores,
            pass_threshold=self._pass_threshold,
            passed=overall_score >= self._pass_threshold,
        )

    @staticmethod
    def save_report(report: BenchmarkTrialReport, file_path: str) -> None:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(asdict(report), ensure_ascii=False, indent=2), encoding="utf-8")
