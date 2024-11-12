from dotenv import load_dotenv

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    HOST: str
    PORT: int


load_dotenv()
config = Config()
