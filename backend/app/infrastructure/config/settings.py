from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


_THIS_DIR = Path(__file__).resolve().parent
_BACKEND_ROOT = _THIS_DIR.parent.parent.parent
_REPO_ROOT = _BACKEND_ROOT.parent


class Settings(BaseSettings):
    service_name: str = "psychology-ai-lab"
    api_version: str = "0.1.0"
    log_level: str = "INFO"
    database_url: str = "sqlite:///./psychology_ai_lab.db"
    provider_timeout_seconds: float = 30.0
    provider_max_retries: int = 2
    provider_retry_delay_seconds: float = 0.2
    openai_api_key: str = ""
    openai_base_url: str = "https://api.openai.com/v1"
    openai_model_name: str = "gpt-4o-mini"
    gemini_api_key: str = ""
    gemini_base_url: str = "https://generativelanguage.googleapis.com/v1beta"
    gemini_model_name: str = "gemini-2.0-flash"

    model_config = SettingsConfigDict(
        env_file=(
            str(_BACKEND_ROOT / ".env"),
            str(_REPO_ROOT / ".env"),
        ),
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
