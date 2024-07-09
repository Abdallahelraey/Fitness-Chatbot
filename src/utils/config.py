from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    GROQ_API_KEY: str
    DATABASE_URL: str
    HUGGING_FACE_API_KEY: str
    MONGO_URI: str
    ASSESMENT_ENDPOINT_URL: str
    LOGIN_RESPONCE_ENDPOINT: str
    ASSESMENT_ENDPOINT_AUTHORIZATION_TOCKEN: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
