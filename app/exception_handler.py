from fastapi import FastAPI, Request, HTTPException, status
from sqlalchemy.exc import IntegrityError


def setup_exception_handles(app: FastAPI) -> FastAPI:
    @app.exception_handler(IntegrityError)
    async def integrity_error(request: Request, exc: IntegrityError):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return app
