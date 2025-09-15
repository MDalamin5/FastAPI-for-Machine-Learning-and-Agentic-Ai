from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Load the .env file
load_dotenv()

class Settings(BaseSettings):
    """Manages Postgres database settings."""

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    JWT_SECRET: str
    JWT_ALGORITHM: str

    @property
    def DATABASE_URL(self) -> str:
        # Encode password to handle special characters
        encoded_password = quote_plus(self.DB_PASSWORD)
        return f"postgresql+asyncpg://{self.DB_USER}:{encoded_password}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        case_sensitive = True
        env_file = ".env"


# Instantiate settings
settings = Settings()

if __name__ == "__main__":
    print(settings.DATABASE_URL)
