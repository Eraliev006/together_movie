
import os
from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    DB_URL: str
    api_prefix: str = '/api/v1'
    PORT: int = 8000
    HOST: str = 'localhost'

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')


settings = Settings()

if __name__ == "__main__":
    print(settings.DB_URL)