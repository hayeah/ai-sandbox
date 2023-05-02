from email import message
import openai

import src.aisandbox as aisandbox
from pprint import pprint


def main():
    cfg = aisandbox.config
    messages = messages = [
        # using this system role makes the output much worse...
        # {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "give one erudite trivia about the byzantines, in markdown format, highlighting the key points"},
    ]

    result = openai.ChatCompletion.create(
        model=cfg.openai.model,
        messages=messages
    )

    pprint(result)


if __name__ == "__main__":
    aisandbox.init()
    main()
