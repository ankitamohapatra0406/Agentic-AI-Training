BLOCKED_OUTPUT=[
    "api key",
    "password",
    "secret",
]


def validate_output(response: str):

    text=response.lower()

    for word in BLOCKED_OUTPUT:

        if word in text:
            return False
    return True