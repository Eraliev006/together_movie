
from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    DB_URL: str

class Settings(BaseSettings):
    db_url: DBSettings = DBSettings()
    api_prefix: str = '/api/v1'
    PORT: int = 8000
    HOST: str = 'localhost'


settings = Settings()