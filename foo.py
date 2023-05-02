import os
import requests
import aiohttp

import openai

if __name__ == "__main__":
    print(requests)
    help(openai)
    print("hello world")
    openai.api_key = os.environ["OPENAI_API_KEY"]

