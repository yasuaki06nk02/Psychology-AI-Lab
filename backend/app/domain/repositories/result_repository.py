from typing import Protocol

from app.domain.entities.result import BenchmarkResult


class ResultRepository(Protocol):
    def save(self, result: BenchmarkResult) -> BenchmarkResult: ...

    def get_by_id(self, result_id: str) -> BenchmarkResult | None: ...

    def list_all(self) -> list[BenchmarkResult]: ...
