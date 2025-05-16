from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models.role import RoleInformation
from app.models.user import LoginRequest, UserResponse

from app.database.user import User

class UserService:
    def __init__(self):
        pass

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

        return UserResponse(
            username=user.username,
            full_name=user.full_name,
            role=RoleInformation(
                id=user.role.id,
                code=user.role.code,
                name=user.role.name
            ) if user.role else None
        )
