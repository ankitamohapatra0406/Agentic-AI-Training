BLOCKED_WORDS=[
    "ignore previous instructions",
    "system prompt",
    "developer message",
    "api key",
    "password",
    "jailbreak",
    "bypass"
]


def validate_input(user_input: str):

    text=user_input.lower()

    for word in BLOCKED_WORDS:

        if word in text:
            return False

    return True