from graph import graph

def main():
    print("=" * 50)
    print("LangGraph Workflow")
    print("=" * 50)

    question=input("\nEnter your question: ")

    result=graph.invoke({
        "question": question
    })

    print("\n" + "=" * 50)
    print("FINAL OUTPUT")
    print("=" * 50)

    print(result["answer"])


if __name__ == "__main__":
    main()