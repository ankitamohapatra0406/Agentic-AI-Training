from datetime import datetime


def log(message):

    with open("logs.txt","a") as file:

        file.write(
            f"{datetime.now()}:{message}\n"
        )