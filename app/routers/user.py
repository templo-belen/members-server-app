from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.middlewares import current_user_ctx
from app.models import UserResponse, AlterUserRequest
from app.services import UserService, AuthService


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
            "/",
            response_model=list[UserResponse] | None,
            dependencies=[Depends(self.auth_service.require_role(['admin']))]
        )
        def get_all(db: Session = Depends(get_db)):
            return self.user_service.get_all(db)
        
        @self.router.post(
            "/",
            response_model=UserResponse | None,
            dependencies=[Depends(self.auth_service.require_role(['admin']))]
        )
        def create_user(user: AlterUserRequest, db: Session = Depends(get_db)):
            return self.user_service.create_user(user, db)
        
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
        
        @self.router.put(
            "/{user_id}",
            response_model=UserResponse | None,
            dependencies=[Depends(self.auth_service.require_role(['admin']))]
        )
        def update_user(user_id: int, user: AlterUserRequest, db: Session = Depends(get_db)):
            return self.user_service.update_user(user_id, user, db)
        
        @self.router.delete(
            "/{user_id}",
            dependencies=[Depends(self.auth_service.require_role(['admin']))]
        )
        def delete_user(user_id: int, db: Session = Depends(get_db)):
            current_user = current_user_ctx.get()
            if user_id == current_user.id:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="El usuario no puede eliminarse a si mismo.")
            self.user_service.delete_user(user_id, db)
