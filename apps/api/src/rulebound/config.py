from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="RULEBOUND_", env_file=".env", extra="ignore")

    env: str = "local"
    database_url: SecretStr = SecretStr(
        "postgresql+asyncpg://rulebound:rulebound@localhost:5432/rulebound"
    )
    log_level: str = "INFO"


@lru_cache
def get_settings() -> Settings:
    return Settings()
