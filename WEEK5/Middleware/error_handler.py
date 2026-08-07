from fastapi.responses import JSONResponse


def handle_error(message):

    return JSONResponse(
        status_code=400,
        content={
            "error": message
        }
    )