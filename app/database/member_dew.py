from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String

from app.database.connection import Base


class MembersDEW(Base):
    __tablename__ = 'members_dew'

    id = Column(Integer, primary_key=True)
    ministration_date = Column(Date)
    worker_1 = Column(String(100))
    worker_2 = Column(String(100))
    is_sharing_testimony = Column(Boolean, default=False)
    is_publishing_testimony = Column(Boolean, default=False)
    is_publishing_testimony_name = Column(Boolean, default=False)
    is_agreed_share_testimony = Column(Boolean, default=False)

    member_id = Column(Integer, ForeignKey('members.id'), unique=True, nullable=False)
