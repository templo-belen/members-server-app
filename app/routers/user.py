from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user import UserResponse
from app.services.auth import AuthService
from app.services.user import UserService


class UserRouter:
    def __init__(self, user_service: UserService, auth_service: AuthService):
        self.auth_service = auth_service
        self.user_service = user_service
        
        self.router = APIRouter(prefix="/users", tags=["users"])
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get(
            "/{user_id}",
            response_model=UserResponse | None,
            dependencies=[Depends(self.auth_service.require_self_or_admin())]
        )
        def get_user(user_id: int, db: Session = Depends(get_db)):
            user_by_id = self.user_service.get_user_information_by_id(user_id, db)
            if not user_by_id:
                raise HTTPException(status_code=403)
            return user_by_id
