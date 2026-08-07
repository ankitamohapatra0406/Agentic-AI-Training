import sqlite3

connection=sqlite3.connect("memory.db")

cursor=connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT
)
""")

connection.commit()
connection.close()