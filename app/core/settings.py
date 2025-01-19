
import os
from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class DBSettings(BaseModel):
    DB_URL: str

class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    api_prefix: str = '/api/v1'
    PORT: int = 8000
    HOST: str = 'localhost'

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')


settings = Settings()

if __name__ == "__main__":
    print(settings.db.DB_URL)