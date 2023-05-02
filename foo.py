from email import message
import openai

import src.aisandbox as aisandbox
from pprint import pprint

from typing import Any


def main():
    cfg = aisandbox.config
    messages = messages = [
        # using this system role makes the output much worse...
        # {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "output in markdown format. give one story about a byzantine historical figure. highlight the key point"},
    ]

    result: Any = openai.ChatCompletion.create(
        model=cfg.openai.model,
        messages=messages
    )

    content: str = result.choices[0].message.content
    finish_reason: str = result.choices[0].finish_reason

    if finish_reason == "content_filter":
        raise Exception("OpenAI content filter blocked the response")
    elif finish_reason == "length":
        content += "...[cutoff]"
    elif finish_reason is None:
        raise Exception("OpenAI returned no finish reason")

    # how to stream result to the terminal?

    print(content)


if __name__ == "__main__":
    aisandbox.init()
    main()
