from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy import Column, Integer, Date, String, Enum, ForeignKey

from app.database import Base
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
    leaving_reason = Column(Enum(LeavingReasonType, name="gender_type", native_enum=True), nullable=True)
    leaving_reason_description = Column(String(100))
    leaving_date = Column(Date)
    acceptance_comment = Column(String(250))
    member_id = Column(Integer, ForeignKey('members.id'), unique=True, nullable=False)

# Pydantic models

class MembersGeneralDataInformation(BaseModel):
    id: int = Field(description="Member general data information DB id")
    member_id: int = Field(description="Member ID", alias="memberId")
    conversion_date: Optional[datetime] = Field(description="Conversion date")
    conversion_place: Optional[str] = Field(description="Convertion place")
    baptism_date: Optional[datetime] = Field(description="Baptism date")
    baptism_place: Optional[str] = Field(description="Baptism place")
    baptism_holy_spirit_date: Optional[datetime] = Field(description="Baptism holy spirit date")
    baptism_holy_spirit_place: Optional[str] = Field(description="Baptism holy spirit place")
    baptism_pastor_name: Optional[str] = Field(description="Baptism pastor name")
    baptism_denomination: Optional[str] = Field(description="Baptism denomination")
    active_member_since: Optional[datetime] = Field(description="Active member since")
    leaving_reason: Optional[LeavingReasonType] = Field(description="Leaving reason")
    leaving_reason_description: Optional[str] = Field(description="Leaving reason")
    leaving_date: Optional[datetime] = Field(description="Leaving date")
    acceptance_comment: Optional[str] = Field(description="Acceptance comment")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )
