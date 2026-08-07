import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from prompt import prompt
from chatbot import retrieve_context

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

print("="*50)
print("Basic LangChain Chatbot")
print("="*50)

while True:

    question=input("\nYou: ")

    if question.lower()=="exit":
        break

    context=retrieve_context(question)

    final_prompt=prompt.format(
        context=context,
        question=question,
    )

    response=llm.invoke(final_prompt)

    print("\nAssistant:")
    print(response.content)