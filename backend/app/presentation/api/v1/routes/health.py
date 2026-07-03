from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.application.services.health_service import HealthService
from app.presentation.api.dependencies import get_health_service

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


@router.get("/health", response_model=HealthResponse)
def health_check(service: HealthService = Depends(get_health_service)) -> HealthResponse:
    health = service.get_health()
    return HealthResponse(
        status=health.status,
        service=health.service,
        version=health.version,
    )
