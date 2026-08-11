from graph import graph

print("=" * 60)
print("MULTI-AGENT CHATBOT")
print("=" * 60)

while True:

    question=input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    initial_state = {
        "question": question,
        "plan": "",
        "agent": "",
        "context": [],
        "response": ""
    }

    result=graph.invoke(initial_state)

    print("\nSelected Agent:", result["agent"])
    print("Plan:", result["plan"])

    print("\nContext:")
    for item in result["context"]:
        print("-", item)

    print("\nResponse:")
    print(result["response"])