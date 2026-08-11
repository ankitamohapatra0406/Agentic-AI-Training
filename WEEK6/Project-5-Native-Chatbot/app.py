from llm import get_response

print("=" * 60)
print("NATIVE CHATBOT")
print("=" * 60)

print("\nType 'exit' to stop.\n")


while True:
    question=input("You: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    if not question.strip():
        continue

    response=get_response(question)

    print("\nAI:", response)
    print()