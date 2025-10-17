from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    EMAIL: str
    FULL_NAME: str
    STACK: str = "Python/FastAPI"
    CATFACT_URL: str = "https://catfact.ninja/fact"
    CATFACT_TIMEOUT_SECONDS: float = 2.0
    FAIL_ON_CATFACT_ERROR: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
