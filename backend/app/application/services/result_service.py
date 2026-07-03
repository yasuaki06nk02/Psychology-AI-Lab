from datetime import UTC, datetime
from uuid import uuid4

from app.domain.entities.result import BenchmarkResult
from app.domain.repositories.result_repository import ResultRepository


class ResultService:
    def __init__(self, repository: ResultRepository) -> None:
        self._repository = repository

    def create(self, benchmark_id: str, model_id: str, score: float) -> BenchmarkResult:
        result = BenchmarkResult(
            id=str(uuid4()),
            benchmark_id=benchmark_id,
            model_id=model_id,
            score=score,
            created_at=datetime.now(UTC),
        )
        return self._repository.save(result)

    def get(self, result_id: str) -> BenchmarkResult | None:
        return self._repository.get_by_id(result_id)

    def list(self) -> list[BenchmarkResult]:
        return self._repository.list_all()
