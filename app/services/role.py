from sqlalchemy.orm import Session

from app.database import Role
from app.models import RoleResponse


class RoleService:
    def __init__(self):
        pass

    def get_all(self, db: Session) -> list[RoleResponse]:
        roles = db.query(Role).all()
        return [RoleResponse.model_validate(role) for role in roles]
