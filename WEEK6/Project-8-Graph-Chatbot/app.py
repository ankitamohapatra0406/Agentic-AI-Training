from graph import graph

print("=" * 60)
print("GRAPH-BASED CHATBOT")
print("=" * 60)
print("\nAsk a question.")
print("Type 'exit' or 'quit' to stop.\n")


while True:
    question=input("You: ").strip()
    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    if not question:
        continue

    result=graph.invoke(
        {
            "question": question,
            "category": "",
            "response": ""
        }
    )
    print("\nCategory:", result["category"])
    print("AI:", result["response"])
    print()