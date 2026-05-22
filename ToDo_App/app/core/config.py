from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "change_this_in_production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./todo.db"

    class Config:
        env_file = ".env"


settings = Settings()
