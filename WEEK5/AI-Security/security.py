BLOCKED_PATTERNS=[
    "ignore previous instructions",
    "system prompt",
    "reveal your instructions",
    "developer message",
    "jailbreak",
    "bypass",
    "disable safety",
    "api key",
]


def detect_prompt_injection(user_input: str):

    text=user_input.lower()

    for pattern in BLOCKED_PATTERNS:

        if pattern in text:
            return True

    return False
