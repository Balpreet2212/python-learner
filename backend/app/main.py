import logging
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app.accounts.router import router as accounts_router
from app.auth.router import router as auth_router
from app.config import settings
from app.content.router import router as content_router
from app.core.errors import AppError
from app.parent.router import router as parent_router
from app.progress.router import router as progress_router

logging.basicConfig(
    level=logging.INFO,
    format='{"time":"%(asctime)s","level":"%(levelname)s","logger":"%(name)s","msg":%(message)s}',
)

app = FastAPI(
    title="PyQuest API",
    version="1.0.0",
    docs_url="/docs" if settings.app_env != "production" else None,
    redoc_url=None,
)

_cors_origins = [
    f"http://{settings.domain}",
    f"https://{settings.domain}",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    *settings.allowed_origins,
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(accounts_router)
app.include_router(progress_router)
app.include_router(content_router)
app.include_router(parent_router)


@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    body: dict[str, object] = {"code": exc.code, "message": exc.app_message}
    if exc.details is not None:
        body["details"] = exc.details
    return JSONResponse(status_code=exc.status_code, content=body)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "version": "1.0.0"}


# Serve built frontend in production (Railway single-service deploy)
_static = Path(__file__).parent / "static"
if _static.is_dir():
    app.mount("/", StaticFiles(directory=str(_static), html=True), name="spa")
