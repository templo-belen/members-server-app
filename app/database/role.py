from sqlalchemy import Column, Integer, String, TIMESTAMP

from app.database.database import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(15), unique=True, index=True)
    name = Column(String(255))
    created_at = Column(TIMESTAMP)
