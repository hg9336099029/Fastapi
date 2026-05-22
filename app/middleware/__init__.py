import logging
import time
import uuid
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

logger = logging.getLogger("merged_app")


def register_app_middleware(app: FastAPI):
    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        request_id = str(uuid.uuid4())
        start_time = time.time()
        # read body safely
        try:
            body_bytes = await request.body()
            try:
                body_text = body_bytes.decode("utf-8")
            except Exception:
                body_text = str(body_bytes)
        except Exception:
            body_text = "<could not read body>"

        logger.info(f"[{request_id}] Incoming request {request.method} {request.url} Body: {body_text}")
        try:
            response = await call_next(request)
        except Exception:
            elapsed = (time.time() - start_time) * 1000
            logger.exception(f"[{request_id}] Error processing request after {elapsed:.2f}ms")
            raise
        process_time = (time.time() - start_time) * 1000
        response.headers["X-Process-Time"] = f"{process_time:.2f}ms"
        logger.info(f"[{request_id}] Outgoing response status_code={response.status_code} path={request.url.path} time_ms={process_time:.2f}")
        return response


def register_exception_handlers(app: FastAPI):
    async def http_exception_handler(request: Request, exc: HTTPException):
        logger.warning(f"HTTPException: {exc.detail}")
        return JSONResponse(status_code=exc.status_code, content={"error": "http_error", "message": str(exc.detail)})

    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logger.warning(f"Validation error: {exc.errors()}")
        return JSONResponse(status_code=422, content={"error": "validation_error", "details": exc.errors()})

    async def value_error_handler(request: Request, exc: ValueError):
        logger.warning(f"ValueError: {str(exc)}")
        return JSONResponse(status_code=400, content={"error": "bad_request", "message": str(exc)})

    async def generic_exception_handler(request: Request, exc: Exception):
        logger.exception("Unhandled exception")
        return JSONResponse(status_code=500, content={"error": "internal_server_error", "message": "An unexpected error occurred."})

    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(ValueError, value_error_handler)
    app.add_exception_handler(Exception, generic_exception_handler)
