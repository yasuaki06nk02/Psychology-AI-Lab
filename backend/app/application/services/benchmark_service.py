from datetime import UTC, datetime
from uuid import uuid4

from app.domain.entities.benchmark import Benchmark
from app.domain.repositories.benchmark_repository import BenchmarkRepository


class BenchmarkService:
    def __init__(self, repository: BenchmarkRepository) -> None:
        self._repository = repository

    def create(self, name: str, dataset_id: str, benchmark_version: str) -> Benchmark:
        benchmark = Benchmark(
            id=str(uuid4()),
            name=name,
            dataset_id=dataset_id,
            benchmark_version=benchmark_version,
            created_at=datetime.now(UTC),
        )
        return self._repository.save(benchmark)

    def get(self, benchmark_id: str) -> Benchmark | None:
        return self._repository.get_by_id(benchmark_id)

    def list(self) -> list[Benchmark]:
        return self._repository.list_all()
