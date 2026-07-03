from fastapi.testclient import TestClient

from app.application.errors import AppError
from app.main import create_app
from app.presentation.api.dependencies import get_health_service


def test_app_error_is_mapped_to_structured_response() -> None:
    app = create_app()

    def broken_dependency() -> None:
        raise AppError(
            code="service_unavailable",
            message="Health service unavailable",
            status_code=503,
        )

    app.dependency_overrides[get_health_service] = broken_dependency
    client = TestClient(app, raise_server_exceptions=False)

    response = client.get("/api/v1/health")

    assert response.status_code == 503
    assert response.json() == {
        "code": "service_unavailable",
        "message": "Health service unavailable",
    }


def test_unexpected_error_is_mapped_to_internal_server_error() -> None:
    app = create_app()

    def broken_dependency() -> None:
        raise RuntimeError("unexpected failure")

    app.dependency_overrides[get_health_service] = broken_dependency
    client = TestClient(app, raise_server_exceptions=False)

    response = client.get("/api/v1/health")

    assert response.status_code == 500
    assert response.json() == {
        "code": "internal_server_error",
        "message": "Internal Server Error",
    }
