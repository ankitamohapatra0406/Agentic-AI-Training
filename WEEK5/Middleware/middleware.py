from fastapi import Request

from logger import log


async def request_middleware(request:Request,call_next):

    log(f"Incoming Request:{request.url}")

    response=await call_next(request)

    log(f"Response Status:{response.status_code}")

    return response