
import os
import json
import tomlkit
from pydantic import BaseModel
from typing import Type, TypeVar

T = TypeVar('T', bound=BaseModel)
def load_from_env(config: Type[T]) -> T:
    config_toml = os.environ.get("CONFIG_TOML")
    config_json = os.environ.get("CONFIG_JSON")

    if config_toml:
        return config.parse_obj(tomlkit.loads(config_toml))
    elif config_json:
        return config.parse_obj(json.loads(config_json))
    else:
        raise Exception("Neither CONFIG_TOML nor CONFIG_JSON was set")
