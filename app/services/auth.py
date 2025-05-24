from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status, Header
from jose import jwt, JWTError
from passlib.context import CryptContext

from app.database import get_db, User, Session
from app.models import TokenResponse, LoginRequest
from app.services.user import UserService
from app.settings import settings

from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.database.user import User

class AuthService:

    _403_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    def __init__(self, user_service: UserService):
        self.user_service = user_service
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, userdata : LoginRequest):
        return self.pwd_context.verify(plain_password, userdata.password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def create_access_token(self, data: LoginRequest, expires_delta: timedelta | None = None):
        to_encode = {"id" : data.id}
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        token_response = TokenResponse(access_token=jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM),
                               token_type="Bearer")
        return token_response
    
    def decode_token(self, authorization):
        if not authorization or not authorization.startswith("Bearer "):
            raise self._403_exception
        token = authorization.split(" ")[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            return payload
        except JWTError as e:
            raise self._403_exception
        
    def get_current_user(self, authorization: str | None = Header(default=None), db: Session = Depends(get_db)) -> User:
        payload = self.decode_token(authorization)
        user_id: int = payload.get("id")
        user = self.user_service.get_user_information_by_id(user_id, db)
        return user
    
    def require_role(self, role_required: list[str]):
        def require_role_dependency(current_user: User = Depends(self.get_current_user)):
            if current_user.role.code not in role_required:
                raise self._403_exception
            return True
        return require_role_dependency
