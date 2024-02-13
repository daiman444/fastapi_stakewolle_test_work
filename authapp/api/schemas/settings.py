import os

from typing import Any, Dict, List, Optional
from pydantic_settings import BaseSettings


if os.path.isfile('.env'):
    from dotenv import load_dotenv
    load_dotenv()
    print('Loading environment variables from .env')
else:
    print("No .env file found. Using system environment variables.")


class Settings(BaseSettings):
    APP_PATH: str
    
settings = Settings()
