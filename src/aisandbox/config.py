import os
# import json
from pydantic import BaseModel


class OpenaiConfig(BaseModel):
    secret: str


class AppConfig(BaseModel):
    openai: OpenaiConfig

def load() -> AppConfig:
    return AppConfig.parse_raw(os.environ.get("CONFIG_JSON", "{}"))
