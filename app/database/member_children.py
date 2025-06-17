from sqlalchemy import Column, ForeignKey, Integer, String

from app.database.connection import Base


class MemberChildren(Base):
    __tablename__ = "members_children"

    id = Column(Integer, primary_key=True, autoincrement=True)
    child_name = Column(String(150), nullable=False)
    child_occupation = Column(String(150))

    member_id = Column(Integer, ForeignKey("members.id"), unique=False, nullable=False)
