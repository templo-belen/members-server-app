from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String

from app.database.connection import Base
from app.models.enum_type import LeavingReasonType


class MembersGeneralData(Base):
    __tablename__ = 'members_general_data'

    id = Column(Integer, primary_key=True)
    conversion_date = Column(Date)
    conversion_place = Column(String(100))
    baptism_date = Column(Date)
    baptism_place = Column(String(100))
    baptism_holy_spirit_date = Column(Date)
    baptism_holy_spirit_place = Column(String(100))
    baptism_pastor_name = Column(String(150))
    baptism_denomination = Column(String(100))
    active_member_since = Column(Date)
    leaving_reason = Column(Enum(LeavingReasonType, name="leaving_reason_type", native_enum=False),
                            nullable=True)
    leaving_reason_description = Column(String(100))
    leaving_date = Column(Date)
    acceptance_comment = Column(String(250))
    member_id = Column(Integer, ForeignKey('members.id'), unique=True, nullable=False)
