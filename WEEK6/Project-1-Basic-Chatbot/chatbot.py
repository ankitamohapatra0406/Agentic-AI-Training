import sqlite3

def retrieve_context(question):

    connection=sqlite3.connect("data.db")

    cursor=connection.cursor()

    cursor.execute(
        "SELECT information FROM knowledge"
    )

    data = cursor.fetchall()

    connection.close()

    return "\n".join(
        row[0]
        for row in data
    )