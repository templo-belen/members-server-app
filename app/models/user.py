from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.role import Role, RoleInformation


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(255))
    full_name = Column(String(200))
    role_id = Column(Integer, ForeignKey("roles.id"))
    created_at = Column(TIMESTAMP)

    role = relationship(Role)

class UserLogin(BaseModel):
    id : int
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserInformation(BaseModel):
    username: str
    full_name: str
    role: RoleInformation | None
