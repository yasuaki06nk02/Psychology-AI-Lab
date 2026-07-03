from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Dataset:
    id: str
    dataset_name: str
    version: str
    question_count: int
    created_at: datetime
