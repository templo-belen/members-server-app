from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.database import Base


class MembersReference(Base):
    __tablename__ = 'members_references'

    id = Column(Integer, primary_key=True)

    total_time = Column(Integer)
    church_name = Column(String(100))
    main_pastor_name = Column(String(150))
    leaving_reason = Column(String(50))

    member_id = Column(Integer, ForeignKey('members.id'), unique=True, nullable=False)
