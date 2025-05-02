from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models.role import RoleInformation
from app.models.user import User, UserLogin, UserInformation


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_login_by_username(self, username: str) -> UserLogin | None:
        stmt = select(User.id, User.username, User.password).where(User.username == username.lower())
        result = self.db.execute(stmt).first()
        if result:
            return UserLogin(id=result.id, username=result.username, password=result.password)
        return None


    def get_user_information_by_id(self, user_id: int) -> UserInformation | None:
        user = self.db.query(User).filter(User.id == user_id).options(joinedload(User.role)).first()

        if not user:
            return None

        return UserInformation(
            username=user.username,
            full_name=user.full_name,
            role=RoleInformation(
                id=user.role.id,
                code=user.role.code,
                name=user.role.name
            ) if user.role else None
        )
