import os

from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_TIME: int = 3600
    REDIS_URL: str

    class Config:
        env_file = Path(__file__).parent / ".env"


settings = Settings()
