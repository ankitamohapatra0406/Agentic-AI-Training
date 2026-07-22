import database
from memory import chat_history, save_memory, load_memory

print("=" * 50)
print("Agent Memory Demo")
print("=" * 50)

question = input("\nAsk a question: ")

answer = f"Sample answer for: {question}"

# Short-Term Memory
chat_history.append((question, answer))

# Long-Term Memory
save_memory(question, answer)

print("\nCurrent Session Memory:")
for q, a in chat_history:
    print(f"Q: {q}")
    print(f"A: {a}")
    print()

print("=" * 50)
print("Stored Database Memory")
print("=" * 50)

records = load_memory()

for record in records:
    print(record)