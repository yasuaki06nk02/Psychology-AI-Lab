from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class BenchmarkResult:
    id: str
    benchmark_id: str
    model_id: str
    score: float
    created_at: datetime
