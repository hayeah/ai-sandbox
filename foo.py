import os
import requests
import aiohttp

import openai
import json

from pydantic import BaseModel


class OpenaiConfig(BaseModel):
    secret: str


class AppConfig(BaseModel):
    openai: OpenaiConfig


# parse CONFIG_JSON into a dict

config = AppConfig.parse_raw(os.environ.get("CONFIG_JSON", "{}"))

if __name__ == "__main__":
    # print(requests)
    # help(openai)
    # print("hello world")
    print(config.openai.secret)
    # openai.api_key = os.environ["OPENAI_API_KEY"]
