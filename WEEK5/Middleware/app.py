from fastapi import FastAPI, Header

from middleware import request_middleware
from auth import authenticate
from logger import log
from rate_limit import allow_request
from error_handler import handle_error

app=FastAPI()

app.middleware("http")(request_middleware)


@app.get("/")
def home():

    return {
        "message": "AI Middleware Running"
    }

@app.get("/chat")
def chat(
    question: str,
    api_key: str = Header(...)
):

    if not authenticate(api_key):

        return handle_error(
            "Invalid API Key"
        )

    if not allow_request(api_key):

        return handle_error(
            "Rate Limit Exceeded"
        )

    log(question)

    return {
        "answer":f"AI Response for: {question}"
    }