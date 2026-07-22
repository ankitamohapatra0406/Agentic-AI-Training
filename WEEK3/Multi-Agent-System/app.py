from graph import graph


def main():
    print("=" * 50)
    print("Multi-Agent System")
    print("=" * 50)

    question = input("\nEnter your task: ")

    result = graph.invoke({
        "question": question
    })

    print("\n" + "=" * 50)
    print(result["review"])


if __name__ == "__main__":
    main()