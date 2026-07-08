from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

from tools import calculator, today

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

tools = [calculator, today]

llm_with_tools = llm.bind_tools(tools)

print("🤖 Tool Calling Chatbot")
print("Type 'exit' to quit.\n")

while True:
    query = input("\nYou: ")

    if query.lower() == "exit":
        break

    response = llm_with_tools.invoke(query)

    # If the LLM wants to use a tool
    if response.tool_calls:

        for tool_call in response.tool_calls:

            if tool_call["name"] == "calculator":

                result = calculator.invoke(tool_call["args"])

                print("\n Calculator Result:", result)

            elif tool_call["name"] == "today":

                result = today.invoke(tool_call["args"])

                print("\n📅 Today's Date:", result)

    else:
        print("\n AI:", response.content)