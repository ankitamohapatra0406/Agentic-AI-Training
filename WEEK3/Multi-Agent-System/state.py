from typing import TypedDict


class AgentState(TypedDict):
    question: str
    research: str
    code: str
    review: str