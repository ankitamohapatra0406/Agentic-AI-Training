import sqlite3

connection = sqlite3.connect("memory.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memory(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
)
""")

connection.commit()
connection.close()