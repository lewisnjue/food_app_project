import os
from pathlib import Path
from functools import lru_cache
from pydantic_settings import BaseSettings

os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = "1"

class Settings(BaseSettings):
    base_dir: Path = Path(__file__).resolve().parent
    keyspace: str 
    db_client_id: str 
    db_client_secret: str 
    secret_key: str
    jwt_algorithm: str 
    session_duration: int 

    class Config:
        env_file = '.env'


@lru_cache
def get_settings():
    return Settings()
