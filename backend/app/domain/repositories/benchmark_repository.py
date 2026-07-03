from typing import Protocol

from app.domain.entities.benchmark import Benchmark


class BenchmarkRepository(Protocol):
    def save(self, benchmark: Benchmark) -> Benchmark: ...

    def get_by_id(self, benchmark_id: str) -> Benchmark | None: ...

    def list_all(self) -> list[Benchmark]: ...
