"""
openai sandbox
"""

import openai

DEFAULT_MODEL = "gpt-3.5-turbo-0301"


def main():
    """
    open ai example
    """

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "give me 3 interesting trivias from medieval europe"},
    ]

    result = openai.ChatCompletion.create(
        model=DEFAULT_MODEL,
        messages=messages
    )



    print("hello world")


if __name__ == "__main__":
    main()
