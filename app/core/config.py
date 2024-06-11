from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Libra Translate API"
    environment: str = "dev"
    testing: bool = 0
    AI_SERVICE_URL: str = "http://iana:8501/v1/models/iana:predict"


settings = Settings()
