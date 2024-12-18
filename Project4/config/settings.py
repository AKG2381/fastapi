from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = "fastapi/Project4/.env"  # Load environment variables from a .env file

# Create an instance of the settings
settings = Settings()
# print(settings.DATABASE_URL)