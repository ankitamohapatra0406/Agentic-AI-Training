from typing import TypedDict, List


class AgentState(TypedDict):
    question: str
    plan: str
    agent: str
    context: List[str]
    response: str