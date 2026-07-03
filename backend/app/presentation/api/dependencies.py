from fastapi import Depends

from app.application.services.health_service import HealthService
from app.infrastructure.config.settings import Settings, get_settings


def get_health_service(settings: Settings = Depends(get_settings)) -> HealthService:
    return HealthService(settings=settings)
