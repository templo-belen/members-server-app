from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base


class MembersReference(Base):
    __tablename__ = 'members_references'

    id = Column(Integer, primary_key=True)

    total_time = Column(Integer)
    church_name = Column(String(100))
    main_pastor_name = Column(String(150))
    leaving_reason = Column(String(50))

    member_id = Column(Integer, ForeignKey('members.id'), unique=True, nullable=False)


# Pydantic models

class MembersReferenceElement(BaseModel):
    id: int = Field(description="Member reference DB id")
    member_id: int = Field(description="Member ID", alias="memberId")

    total_time: Optional[int] = Field(description="Total time reference", alias="totalTime")
    church_name: Optional[str] = Field(description="Reference church name", alias="churchName")
    main_pastor_name: Optional[str] = Field(description="Reference main pastor name", alias="mainPastorName")
    leaving_reason: Optional[str] = Field(description="Leaving reason", alias="leavingReason")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )


class MembersReferenceInformation(BaseModel):
    references: Optional[List[MembersReferenceElement]] = Field(default=None, description="Member's reference list", )
    reasons_for_congregating: Optional[str] = Field(default=None, description="Reason why the member congregates",
                                                    alias="reasonsForCongregating")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )
