import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools import calculate, search_information, database_lookup

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

def generate_response(question, context):
    prompt=f"""
You are a helpful AI assistant.

Answer the user's question using the information provided by the
specialized agent.

Question:
{question}

Agent Information:
{context}

Give a clear and concise answer.
"""
    response = llm.invoke(prompt)

    return response.content


def research_agent(state):
    question=state["question"]

    result=search_information(question)

    response=generate_response(
        question,
        result
    )
    return {
        "context": [result],
        "response": response
    }


def database_agent(state):
    question=state["question"]

    result=database_lookup(question)

    response=generate_response(
        question,
        result
    )
    return {
        "context": [result],
        "response": response
    }


def tool_agent(state):
    question=state["question"]
    expression=question.lower()

    replacements={
        "calculate": "",
        "what is": "",
        "multiply": "*",
        "multiplied by": "*",
        "times": "*",
        "plus": "+",
        "minus": "-",
        "divided by": "/"
    }

    for word, symbol in replacements.items():
        expression = expression.replace(word, symbol)

    result=calculate(expression)
    response=generate_response(
        question,
        result
    )

    return {
        "context": [result],
        "response": response
    }