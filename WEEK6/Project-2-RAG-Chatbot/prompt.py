from langchain_core.prompts import ChatPromptTemplate


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