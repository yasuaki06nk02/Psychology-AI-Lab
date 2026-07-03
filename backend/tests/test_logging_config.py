import logging

from app.infrastructure.logging.config import configure_logging


def test_configure_logging_sets_level() -> None:
    configure_logging("DEBUG")

    assert logging.getLogger().getEffectiveLevel() <= logging.DEBUG
