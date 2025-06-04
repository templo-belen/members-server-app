from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.orm import joinedload, Session

from app.database import User
from app.models import (
    CreateUserRequest,
    LoginRequest,
    UserResponse,
)


class UserService:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, userdata : LoginRequest):
        return self.pwd_context.verify(plain_password, userdata.password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def get_all(self, db: Session) -> list[UserResponse]:
        users = db.query(User).all()
        return [UserResponse.model_validate(user) for user in users]

    def get_user_login_by_username(self, username: str, db: Session) -> LoginRequest | None:
        stmt = select(User.id, User.username, User.password).where(User.username == username.lower())
        result = db.execute(stmt).first()
        if result:
            return LoginRequest(id=result.id, username=result.username, password=result.password)
        return None


    def get_user_information_by_id(self, user_id: int, db: Session) -> UserResponse | None:
        user = db.query(User).filter(User.id == user_id).options(joinedload(User.role)).first()
        if not user:
            return None
        return UserResponse.model_validate(user)
    
    def create_user(self, new_user: CreateUserRequest, db: Session) -> UserResponse:
        db_user = User(**new_user.model_dump(exclude_unset=True),)
        db_user.password = self.get_password_hash(new_user.password)

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return UserResponse.model_validate(db_user)
