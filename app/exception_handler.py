from fastapi import FastAPI, Request, HTTPException, status
from sqlalchemy.exc import IntegrityError

from app.services import LogicConstraintViolationException


def setup_exception_handles(app: FastAPI) -> FastAPI:
    @app.exception_handler(IntegrityError)
    async def integrity_error(request: Request, exc: IntegrityError):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @app.exception_handler(LogicConstraintViolationException)
    async def logic_constraint_violation_exception(request: Request, exc: LogicConstraintViolationException):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=exc.message)

    return app
