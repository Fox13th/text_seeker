import os
from functools import lru_cache
from logging import config as logging_config

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

from src.core.logger import LOGGING

env_file_path = '.env'
if not os.path.exists(env_file_path):
    raise TypeError(f'Env file not found. Path: "{env_file_path}"')
load_dotenv(dotenv_path=env_file_path)


class Settings(BaseSettings):
    # App Settings
    project_name: str = 'recognition_service'
    base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    app_host: str = '0.0.0.0'
    app_port: int = 8000

    # Redis Settings

    # Postgres Settings
    # Utils Settings
    logging_config.dictConfig(LOGGING)

    # Authorization Settings
    #jwt_secret_key: str
    #jwt_algorithm: str

    debug: bool = False

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache(maxsize=None)
def get_settings():
    """Получаем настройки приложения, сохраняя в кэш."""
    return Settings(_env_file=env_file_path)
