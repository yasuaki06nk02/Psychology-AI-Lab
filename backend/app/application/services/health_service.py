from app.domain.entities.health_status import HealthStatus
from app.infrastructure.config.settings import Settings


class HealthService:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def get_health(self) -> HealthStatus:
        return HealthStatus(
            status="ok",
            service=self._settings.service_name,
            version=self._settings.api_version,
        )
