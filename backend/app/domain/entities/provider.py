from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Provider:
    id: str
    name: str
    display_name: str
    created_at: datetime
