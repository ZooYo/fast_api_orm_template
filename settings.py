from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv


class Settings(BaseSettings):
    database_url: str
    migration_database_url: str

    class Config:
        env_file = "./env/.env.dev"


# Load the .env file
env_path = Path("./env") / ".env.dev"
load_dotenv(dotenv_path=env_path)

settings = Settings()
