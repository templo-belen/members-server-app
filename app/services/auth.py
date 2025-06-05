from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException, status, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import TokenResponse, LoginRequest, UserResponse
from app.services.user import UserService
from app.settings import settings


class AuthService:

    _403_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def create_access_token(self, data: LoginRequest, expires_delta: timedelta | None = None):
        to_encode = {"id" : data.id}
        expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        token_response = TokenResponse(access_token=jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM),
                               token_type="Bearer")
        return token_response
    
    def decode_token(self, authorization):
        if not authorization or not authorization.startswith("Bearer "):
            raise self._403_exception
        token = authorization.split(" ")[1]
        try:
            return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        except JWTError as e:
            raise self._403_exception

    def get_current_user(self, authorization: str | None = Header(default=None), db: Session = Depends(get_db)) -> UserResponse | None:
        payload = self.decode_token(authorization)
        return self.user_service.get_user_information_by_id(payload.get("id"), db)

    def require_role(self, role_required: list[str]):
        def require_role_dependency(auth: HTTPAuthorizationCredentials = Depends(HTTPBearer()), db: Session = Depends(get_db)):
            current_user = self.get_current_user(f"Bearer {auth.credentials}", db)
            if current_user.role.code not in role_required:
                raise self._403_exception
            return True
        return require_role_dependency
    
    def require_self_or_admin(self):
        def require_self_or_admin_dependency(user_id: int, auth: HTTPAuthorizationCredentials = Depends(HTTPBearer()), db: Session = Depends(get_db)):
            payload = self.decode_token(f"Bearer {auth.credentials}")
            current_user_id = payload.get('id')
            current_user = self.user_service.get_user_information_by_id(current_user_id, db)
            if current_user_id != user_id and (not current_user or current_user.role.code != 'admin'):
                raise self._403_exception
            return True
        return require_self_or_admin_dependency
