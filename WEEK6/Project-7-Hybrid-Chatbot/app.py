from hybrid_search import hybrid_search
from llm import generate_response


print("=" * 60)
print("HYBRID CHATBOT")
print("=" * 60)
print("\nAsk questions about the knowledge base.")
print("Type 'exit' to stop.\n")


while True:
    question=input("You: ").strip()
    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    if not question:
        continue
    print("\nSearching...")

    results=hybrid_search(question)

    context="\n\n".join(
        document.page_content
        for document in results
    )
    response=generate_response(
        question,
        context
    )
    print("\nAI:", response)
    print()