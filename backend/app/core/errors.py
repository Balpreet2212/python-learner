"""Consistent error response shape per §11.1: {code, message, details?}"""

from fastapi import HTTPException
from fastapi.responses import JSONResponse


class AppError(HTTPException):
    def __init__(self, status_code: int, code: str, message: str, details: object = None) -> None:
        self.code = code
        self.app_message = message
        self.details = details
        super().__init__(status_code=status_code, detail=message)


def error_response(code: str, message: str, details: object = None) -> JSONResponse:
    body: dict[str, object] = {"code": code, "message": message}
    if details is not None:
        body["details"] = details
    return JSONResponse(status_code=400, content=body)


# Common pre-built errors
def not_found(resource: str = "Resource") -> AppError:
    return AppError(404, "not_found", f"{resource} not found")


def unauthorized(message: str = "Authentication required") -> AppError:
    return AppError(401, "unauthorized", message)


def forbidden(message: str = "Forbidden") -> AppError:
    return AppError(403, "forbidden", message)


def conflict(message: str) -> AppError:
    return AppError(409, "conflict", message)


def bad_request(message: str, details: object = None) -> AppError:
    return AppError(400, "bad_request", message, details)


def rate_limited() -> AppError:
    return AppError(429, "rate_limited", "Too many requests. Please try again later.")
