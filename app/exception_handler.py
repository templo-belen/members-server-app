from fastapi import FastAPI, HTTPException, Request, status
from sqlalchemy.exc import IntegrityError

from app.services import ConflictException, LogicConstraintViolationException, NotFoundException


def setup_exception_handles(app: FastAPI) -> FastAPI:
    @app.exception_handler(IntegrityError)
    async def integrity_error(request: Request, exc: IntegrityError):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @app.exception_handler(LogicConstraintViolationException)
    async def logic_constraint_violation_exception(request: Request, exc: LogicConstraintViolationException):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=exc.message)

    @app.exception_handler(NotFoundException)
    async def not_found_exception(request: Request, exc: NotFoundException):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)

    @app.exception_handler(ConflictException)
    async def conflict_exception(request: Request, exc: ConflictException):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=exc.message)

    return app
