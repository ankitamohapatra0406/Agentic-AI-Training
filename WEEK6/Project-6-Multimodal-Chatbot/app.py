from multimodal import analyze_image


print("=" * 60)
print("MULTIMODAL CHATBOT")
print("=" * 60)

image_path=input("\nEnter image path: ").strip()

print("\nImage loaded.")
print("Ask questions about the image.")
print("Type 'exit' to stop.\n")


while True:
    question=input("You: ").strip()

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    if not question:
        continue

    print("\nAI is analyzing the image...")
    try:
        response=analyze_image(
            image_path,
            question
        )
        print("\nAI:", response)
        print()

    except Exception as e:
        print("\nError:", e)
        print()