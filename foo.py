import openai

import src.aisandbox as aisandbox
from pprint import pprint

from typing import Any

from rich.console import Console
from rich.markdown import Markdown

console = Console()


def main():
    cfg = aisandbox.config
    messages = messages = [
        # using this system role makes the output much worse...
        # {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "output in markdown format. give one story about a roman historical figure. bold every name when they first appear"},
    ]

    result: Any = openai.ChatCompletion.create(
        model=cfg.openai.model,
        messages=messages
    )

    pprint(result)

    content: str = result.choices[0].message.content
    finish_reason: str = result.choices[0].finish_reason

    if finish_reason == "content_filter":
        raise Exception("OpenAI content filter blocked the response")
    elif finish_reason == "length":
        content += "...[cutoff]"
    elif finish_reason is None:
        raise Exception("OpenAI returned no finish reason")

    # how to stream result to the terminal?
    console.print(Markdown(content))


def streamit():
    cfg = aisandbox.config
    messages = messages = [
        # using this system role makes the output much worse...
        # {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "output in markdown format. give one story about an interesting historical artifact"},
    ]

    result: Any = openai.ChatCompletion.create(
        model=cfg.openai.model,
        messages=messages,
        # max_tokens=50,
        # n=1,
        # stop=None,
        # temperature=0.5,
        stream=True
    )

    for message in result:
        # chat.completion.chunk
        if message["object"] == "chat.completion.chunk":
            delta = message["choices"][0]["delta"]
            if "content" in delta:
                print(delta["content"], end="", flush=True)

            finish_reason = message["choices"][0]["finish_reason"]
            if finish_reason == "content_filter":
                print("\n[OpenAI content filter blocked the response]")
            elif finish_reason == "length":
                print("\n[cutoff]")
            elif finish_reason == "stop":
                print("\n")
        else:
            print(message)


if __name__ == "__main__":
    aisandbox.init()
    streamit()
    # main()
