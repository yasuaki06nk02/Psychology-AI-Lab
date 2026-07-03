from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.services.health_service import HealthService
from app.infrastructure.config.settings import Settings, get_settings
from app.infrastructure.database.session import get_db


def get_health_service(settings: Settings = Depends(get_settings)) -> HealthService:
    return HealthService(settings=settings)


def get_db_session(db: Session = Depends(get_db)) -> Session:
    return db
