from pydantic import BaseSettings


class Settings(BaseSettings):
    database_name: str
    db_username: str
    db_password: str
    host: str
    authentication_source: str

    class Config:
        env_file = ".env"
