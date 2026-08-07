import sqlite3

def add(a:int, b:int):
    return a+b


def multiply(a:int, b:int):
    return a*b


def read_notes():
    with open("notes.txt","r") as file:
        return file.read()


def save_user(name:str):

    connection=sqlite3.connect("memory.db")
    cursor=connection.cursor()

    cursor.execute(
        "INSERT INTO users(name) VALUES(?)",
        (name,)
    )

    connection.commit()
    connection.close()

    return "User Saved"


def get_users():

    connection=sqlite3.connect("memory.db")
    cursor=connection.cursor()

    cursor.execute("SELECT * FROM users")

    data=cursor.fetchall()

    connection.close()

    return data