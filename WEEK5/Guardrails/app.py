import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from input_guard import validate_input
from output_guard import validate_output
from prompts import SYSTEM_PROMPT

load_dotenv()

llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

print("="*50)
print("Guardrails Demo")
print("="*50)

while True:

    question=input("\nYou: ")

    if question.lower()=="exit":
        break

    if not validate_input(question):

        print("\nInput blocked.")
        continue

    response=llm.invoke(
        SYSTEM_PROMPT + "\n\nUser: " + question
    )

    answer=response.content

  
    if not validate_output(answer):
        print("\nOutput blocked.")

    else:
        print("\nAssistant:")
        print(answer)