from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.database import User
from app.models import CreateUpdateUserRequest, LoginRequest, PasswordChangeRequest, UserResponse
from app.services.exception import LogicConstraintViolationException, NotFoundException
from app.services.pydantic_tools import apply_updates_from_pydantic


class UserService:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def normalize_name(self, name: str) -> str:
        name = name.strip().title()
        while "  " in name:
            name = name.replace("  ", " ")
        return name

    def normalize_user(self, user: User):
        user.username = user.username.lower()
        user.full_name = self.normalize_name(user.full_name)
        user.password = self.get_password_hash(user.password)

    def get_all(self, db: Session) -> list[UserResponse]:
        users = db.query(User).all()
        return [UserResponse.model_validate(user) for user in users]

    def get_user_login_by_username(self, username: str, db: Session) -> LoginRequest | None:
        username = username.lower()
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

    def create_user(self, new_user: CreateUpdateUserRequest, db: Session) -> UserResponse:
        db_user = User(**new_user.model_dump(exclude_unset=True))
        self.normalize_user(db_user)

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return UserResponse.model_validate(db_user)

    def update_user(self, user_id, user: CreateUpdateUserRequest, db: Session) -> UserResponse:
        user_to_update = db.query(User).filter(User.id == user_id).first()
        if not user_to_update:
            raise NotFoundException(f"El usuario con ID {user_id} no existe.")

        apply_updates_from_pydantic(user_to_update, user)
        self.normalize_user(user_to_update)

        db.commit()
        db.refresh(user_to_update)

        return UserResponse.model_validate(user_to_update)

    def delete_user(self, user_id, db: Session):
        user_to_delete = db.get(User, user_id)
        if not user_to_delete:
            raise NotFoundException("El usuario no existe.")

        db.delete(user_to_delete)
        db.commit()

    def password_change(self, user_id, pass_chg: PasswordChangeRequest, db: Session):
        user_to_update = db.query(User).filter(User.id == user_id).first()
        if not user_to_update:
            raise NotFoundException("El usuario con no existe.")

        if not self.verify_password(pass_chg.current_password, user_to_update.password):
            raise LogicConstraintViolationException("Acción no permitida.")

        user_to_update.password = self.get_password_hash(pass_chg.new_password)
        db.commit()
