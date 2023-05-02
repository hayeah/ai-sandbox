import openai
from .config import load_from_env
from pydantic import BaseModel


class OpenAIConfig(BaseModel):
    secret: str
    model: str


class AppConfig(BaseModel):
    openai: OpenAIConfig


def load_config() -> AppConfig:
    return load_from_env(AppConfig)

config = load_config()

def init():
    openai.api_key = config.openai.secret

