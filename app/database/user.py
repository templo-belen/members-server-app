from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

from app.database.database import Base
from app.database.role import Role


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(255))
    full_name = Column(String(200))
    role_id = Column(Integer, ForeignKey("roles.id"))
    created_at = Column(TIMESTAMP)

    role = relationship(Role)
