import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    FRONTEND_URL: str

    class Config:
        env_file = ".env" if os.path.exists(".env") else f".env.{os.getenv('ENV', 'dev')}"


settings = Settings()
