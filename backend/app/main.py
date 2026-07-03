from fastapi import FastAPI

from app.presentation.api.v1.routes.health import router as health_router


def create_app() -> FastAPI:
    app = FastAPI(title="Psychology AI Lab API", version="0.1.0")
    app.include_router(health_router, prefix="/api/v1", tags=["health"])
    return app


app = create_app()
