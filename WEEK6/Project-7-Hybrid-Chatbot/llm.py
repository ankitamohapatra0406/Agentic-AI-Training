import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm=ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_response(question, context):
    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the context, say:
"I don't know based on the provided information."

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content