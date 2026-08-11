import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client=Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def get_response(user_message):
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        temperature=0.7
    )
    return response.choices[0].message.content