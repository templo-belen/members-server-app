from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import LoginResponse
from app.services import AuthService, UserService


class LoginRouter:
    def __init__(self, user_service: UserService, auth_service: AuthService):
        self.auth_service = auth_service
        self.user_service = user_service

        self.router = APIRouter(tags=["login"])
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.post("/login", response_model=LoginResponse)
        def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
            user = self.user_service.get_user_login_by_username(form_data.username, db)
            if not user or not self.user_service.verify_password(form_data.password, user.password):
                raise HTTPException(status_code=401, detail="Invalid credentials")

            token = self.auth_service.create_access_token(user)
            headers = {"Access-Control-Expose-Headers": "Authorization", "Authorization": token.access_token}
            user = self.user_service.get_user_information_by_id(user.id, db)
            content = jsonable_encoder(
                LoginResponse(fullName=user.full_name, username=user.username, features=user.features_list)
            )
            return JSONResponse(content=content, headers=headers)
