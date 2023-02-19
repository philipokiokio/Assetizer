from pydantic import BaseSettings


class DBSettings(BaseSettings):
    name: str
    host: str
    port: int
    password: str
    username: str

    class Config:
        env_file = ".env"


db_settings = DBSettings()
