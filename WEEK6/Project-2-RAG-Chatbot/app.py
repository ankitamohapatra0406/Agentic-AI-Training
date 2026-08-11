import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from rag import retrieve_documents


load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Answer the user's question using ONLY the context provided below.

If the answer is not present in the context, say:
"I don't know based on the provided information."

Context:
{context}

Question:
{question}
""")

while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    documents = retrieve_documents(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    messages = prompt.format_messages(
        context=context,
        question=question
    )

    response = llm.invoke(messages)

    print("\nAI:", response.content)