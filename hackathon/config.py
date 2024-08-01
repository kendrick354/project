from dotenv import load_dotenv
import os
from pydantic import BaseSettings

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PORT: int = int(os.getenv("PORT_NUMBER", 8000))
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    CONNECTION_URL: str = os.getenv("CONNECTION_URL")

    class Config:
        case_sensitive = True

# Initialize settings
settings = Settings()

config = settings
