from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Argus"
    ENVIRONMENT: str = "local"
    DATABASE_URL: str = "postgresql://postgres:postgres_password@localhost:5432/argus"

    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )


settings = Settings()
