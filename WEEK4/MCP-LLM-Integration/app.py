import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from tools import (
    add,
    multiply,
    read_notes,
    save_user,
    get_users,
)

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

tools = [
    add,
    multiply,
    read_notes,
    save_user,
    get_users,
]

tool_map = {
    tool.name: tool
    for tool in tools
}

llm = llm.bind_tools(tools)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    response = llm.invoke(question)

    if response.tool_calls:

        tool_call = response.tool_calls[0]

        tool_name = tool_call["name"]

        args = tool_call["args"]

        result = tool_map[tool_name].invoke(args)

        print("\nTool Used:", tool_name)
        print("Result:", result)

    else:

        print("\nAssistant:", response.content)