from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Experiment:
    id: str
    name: str
    description: str
    created_at: datetime
