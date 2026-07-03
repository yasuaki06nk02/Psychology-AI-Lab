from app.infrastructure.database.session import create_db_engine, create_session_factory


def test_create_db_engine_uses_configured_url() -> None:
    engine = create_db_engine("sqlite:///:memory:")

    assert str(engine.url) == "sqlite:///:memory:"


def test_create_session_factory_creates_sessions() -> None:
    engine = create_db_engine("sqlite:///:memory:")
    session_factory = create_session_factory(engine)

    with session_factory() as session:
        assert session.bind is engine
