"""Application settings, loaded from environment variables / .env file."""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # App
    PROJECT_NAME: str = "Products API"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"
    CORS_ORIGINS: list[str] = [
      "http://localhost:5173",
      "http://127.0.0.1:5173",
  ]

    # Database
    SQLITE_DB_PATH: str = "products.db"
    DB_ECHO: bool = False

    @property
    def db_file(self) -> Path:
        path = Path(self.SQLITE_DB_PATH)
        return path if path.is_absolute() else BASE_DIR / path

    @property
    def sync_database_url(self) -> str:
        """Used by the application (sync SQLAlchemy ORM)."""
        return f"sqlite:///{self.db_file}"

    @property
    def async_database_url(self) -> str:
        """Used by Alembic (async engine via aiosqlite)."""
        return f"sqlite+aiosqlite:///{self.db_file}"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
