from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import UserInformation
from app.services.user import UserService


class UserRouter:
    def __init__(self):
        self.router = APIRouter(tags=["users"])
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get("/users/{user_id}", response_model=UserInformation | None)
        def get_user( user_id: int, db: Session = Depends(get_db)):
            user_service = UserService(db)
            user_by_id = user_service.get_user_information_by_id(user_id)
            if not user_by_id:
                raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
            return user_by_id
