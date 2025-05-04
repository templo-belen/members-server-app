from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import UserInformation
from app.services.user import UserService
from app.services.auth import AuthService


class UserRouter:
    def __init__(self):
        self.router = APIRouter(prefix="/users", tags=["users"])
        self.auth_service = AuthService()
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get(
            "/{user_id}",
            response_model=UserInformation | None,
            # Esto funciona, por ahora estaremos sin seguridad para agilizar
            # Descomentar para agregar autorización
            #dependencies=[Depends(self.auth_service.require_role(["admin"]))]
        )
        def get_user(user_id: int, db: Session = Depends(get_db)):
            user_service = UserService(db)
            user_by_id = user_service.get_user_information_by_id(user_id)
            if not user_by_id:
                raise HTTPException(status_code=403)
            return user_by_id
