from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from llm import generate_response

class ChatState(TypedDict):
    question: str
    category: str
    response: str


def classify_question(state: ChatState):
    question=state["question"].lower()

    technical_words =[
        "python",
        "java",
        "code",
        "programming",
        "machine learning",
        "ai",
        "langchain",
        "langgraph",
        "database"
    ]

    if any(word in question for word in technical_words):
        category="technical"
    else:
        category="general"

    return {
        "category": category
    }

def general_response(state: ChatState):

    response=generate_response(
        state["question"]
    )

    return {
        "response": response
    }

def technical_response(state: ChatState):

    prompt= f"""
You are a technical AI assistant.
Give a clear and beginner-friendly technical explanation.

Question:
{state["question"]}
"""

    response = generate_response(prompt)

    return {
        "response": response
    }

def route_question(state: ChatState):

    if state["category"] == "technical":
        return "technical"

    return "general"

# Build Graph
workflow = StateGraph(ChatState)

workflow.add_node(
    "classify",
    classify_question
)

workflow.add_node(
    "general",
    general_response
)

workflow.add_node(
    "technical",
    technical_response
)


workflow.add_edge(
    START,
    "classify"
)


workflow.add_conditional_edges(
    "classify",
    route_question,
    {
        "general": "general",
        "technical": "technical"
    }
)


workflow.add_edge(
    "general",
    END
)

workflow.add_edge(
    "technical",
    END
)

graph = workflow.compile()