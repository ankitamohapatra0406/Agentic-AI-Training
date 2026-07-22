import sqlite3

# Short-Term Memory
chat_history = []


def save_memory(question, answer):
    connection = sqlite3.connect("memory.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO memory(question, answer) VALUES (?, ?)",
        (question, answer)
    )

    connection.commit()
    connection.close()


def load_memory():
    connection = sqlite3.connect("memory.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM memory")

    data = cursor.fetchall()

    connection.close()

    return data