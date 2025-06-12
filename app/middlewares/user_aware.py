from contextvars import ContextVar

from fastapi import Request
from fastapi.logger import logger
from starlette.middleware.base import BaseHTTPMiddleware

from app.database import User, get_db
from app.services import AuthService

current_user_ctx: ContextVar[User | None] = ContextVar("current_user", default=None)

class UserAwareMiddleware(BaseHTTPMiddleware):
    """
    This middleware extracts the user data from the JWT if any and add it the request context.
    
    In case there is no token or any other failure, this middleware won't block the request.
    """
    def __init__(self, app, auth_service: AuthService):
        super().__init__(app)
        self.auth_service = auth_service

    async def dispatch(self, request: Request, call_next):
        try:
            authorization = request.headers.get('Authorization')
            current_user = self.auth_service.get_current_user(authorization, next(get_db()))
            current_user_ctx.set(current_user)
        except Exception as e:
            logger.warning(f"Error inesperado al obtener el usuario: {e}")
            pass

        return await call_next(request)
