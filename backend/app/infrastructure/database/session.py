from collections.abc import Generator
from functools import lru_cache

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from app.infrastructure.config.settings import get_settings


def create_db_engine(database_url: str) -> Engine:
    return create_engine(database_url, future=True)


def create_session_factory(engine: Engine) -> sessionmaker[Session]:
    return sessionmaker(bind=engine, autoflush=False, autocommit=False)


@lru_cache
def get_engine() -> Engine:
    settings = get_settings()
    return create_db_engine(settings.database_url)


@lru_cache
def get_session_factory() -> sessionmaker[Session]:
    return create_session_factory(get_engine())


def get_db() -> Generator[Session, None, None]:
    session_factory = get_session_factory()
    with session_factory() as session:
        yield session


def check_database_connection(engine: Engine) -> bool:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return True
