from langchain.tools import tool
import sqlite3

@tool
def add(a:int, b:int)->int:
    """Add two numbers."""
    return a + b


@tool
def multiply(a:int, b:int)->int:
    """Multiply two numbers."""
    return a*b


@tool
def read_notes()->str:
    """Read notes from notes.txt."""

    with open("notes.txt", "r") as file:
        return file.read()


@tool
def save_user(name: str)->str:
    """Save a user into the database."""

    connection=sqlite3.connect("memory.db")
    cursor=connection.cursor()

    cursor.execute(
        "INSERT INTO users(name) VALUES(?)",
        (name,)
    )

    connection.commit()
    connection.close()

    return "User saved successfully."


@tool
def get_users()->str:
    """Retrieve all users."""

    connection=sqlite3.connect("memory.db")
    cursor=connection.cursor()

    cursor.execute("SELECT * FROM users")

    users=cursor.fetchall()

    connection.close()

    return str(users)