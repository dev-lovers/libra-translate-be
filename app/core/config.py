from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Libra Translate API"
    environment: str = "dev"
    testing: bool = 0


settings = Settings()
