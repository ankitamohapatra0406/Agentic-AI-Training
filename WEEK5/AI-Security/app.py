import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from security import detect_prompt_injection
from prompts import SYSTEM_PROMPT

load_dotenv()

llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

print("="*50)
print("Secure AI Assistant")
print("="*50)

while True:

    question=input("\nYou: ")

    if question.lower()=="exit":
        break

    if detect_prompt_injection(question):

        print("\nPrompt Injection Detected.")
        continue

    response=llm.invoke(
        SYSTEM_PROMPT + "\n\nUser: " + question
    )

    print("\nAssistant:")
    print(response.content)