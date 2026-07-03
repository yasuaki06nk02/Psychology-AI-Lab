from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Benchmark:
    id: str
    name: str
    dataset_id: str
    benchmark_version: str
    created_at: datetime
