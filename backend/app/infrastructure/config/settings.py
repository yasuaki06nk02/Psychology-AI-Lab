from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


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

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
