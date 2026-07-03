from fastapi import FastAPI

from app.infrastructure.config.settings import get_settings
from app.infrastructure.logging.config import configure_logging
from app.presentation.api.exception_handlers import register_exception_handlers
from app.presentation.api.v1.routes.health import router as health_router


def create_app() -> FastAPI:
    settings = get_settings()
    configure_logging(settings.log_level)

    app = FastAPI(title="Psychology AI Lab API", version=settings.api_version)
    register_exception_handlers(app)
    app.include_router(health_router, prefix="/api/v1", tags=["health"])
    return app


app = create_app()
