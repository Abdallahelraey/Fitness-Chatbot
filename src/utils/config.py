from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    GROQ_API_KEY: str
    DATABASE_URL: str
    HUGGING_FACE_API_KEY: str
    MONGO_URI: str

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
