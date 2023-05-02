import os
import requests
import aiohttp

import openai


# parse CONFIG_JSON into a dict

# import config from config.py

import src.aisandbox as aisandbox

# .config as config



if __name__ == "__main__":
    cfg = aisandbox.config.load()
    # cfg = aisandbox.load_config()
    # print(requests)
    # help(openai)
    # print("hello world")
    print(cfg.openai.secret)
    # openai.api_key = os.environ["OPENAI_API_KEY"]
