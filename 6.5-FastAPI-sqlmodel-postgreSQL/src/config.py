from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv()

class Settings(BaseSettings):
    POSTGRES_URL: str  # Changed from POSTGRES_URL

    model_config = SettingsConfigDict(
        env_file = ".env",
        extra="ignore"
    )

settings = Settings()

print(settings.model_dump())