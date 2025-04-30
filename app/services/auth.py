from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from app.models.user import Token, UserLogin
from app.settings import settings


class AuthService:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, userdata : UserLogin):
        return self.pwd_context.verify(plain_password, userdata.password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def create_access_token(self, data: UserLogin, expires_delta: timedelta | None = None):
        to_encode = {"id" : data.id}
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        token_response = Token(access_token=jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM),
                               token_type="Bearer")
        return token_response

