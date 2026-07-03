from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class AIModel:
    id: str
    provider_id: str
    model_name: str
    version: str
    created_at: datetime
