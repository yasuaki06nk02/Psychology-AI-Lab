from app.infrastructure.database.session import (
    check_database_connection,
    create_db_engine,
    create_session_factory,
)


def test_database_connection_check_returns_true() -> None:
    engine = create_db_engine("sqlite:///:memory:")

    assert check_database_connection(engine) is True


def test_session_factory_creates_session_bound_to_engine() -> None:
    engine = create_db_engine("sqlite:///:memory:")
    session_factory = create_session_factory(engine)

    with session_factory() as session:
        assert session.bind is engine
