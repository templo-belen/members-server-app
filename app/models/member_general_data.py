from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

from app.models.enum_type import LeavingReasonType


class MemberGeneralDataResponse(BaseModel):
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
