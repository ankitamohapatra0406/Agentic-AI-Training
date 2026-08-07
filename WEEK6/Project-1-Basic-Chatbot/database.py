import sqlite3

connection=sqlite3.connect("data.db")

cursor=connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS knowledge(
id INTEGER PRIMARY KEY AUTOINCREMENT,
topic TEXT,
information TEXT
)
""")

cursor.execute("""
INSERT INTO knowledge(topic,information)
VALUES
(
'AI',
'Artificial Intelligence enables machines to perform tasks requiring human intelligence.'
)
""")

connection.commit()
connection.close()

print("Database Created")