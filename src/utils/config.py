from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    GROQ_API_KEY: str
    DATABASE_URL: str


    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
