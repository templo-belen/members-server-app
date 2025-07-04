from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from app.models.enum_serializer import serialized_enum_by_name
from app.models.enum_type import LeavingReasonType


class MemberGeneralDataResponse(BaseModel):
    id: int = Field(description="Member general data information DB id")
    member_id: int = Field(description="Member ID", alias="memberId")
    conversion_date: Optional[date] = Field(description="Conversion date", alias="conversionDate")
    conversion_place: Optional[str] = Field(description="Convertion place", alias="conversionPlace")
    baptism_date: Optional[date] = Field(description="Baptism date", alias="baptismDate")
    baptism_place: Optional[str] = Field(description="Baptism place", alias="baptismPlace")
    baptism_holy_spirit_date: Optional[date] = Field(
        description="Baptism holy spirit date", alias="baptismHolySpiritDate"
    )
    baptism_holy_spirit_place: Optional[str] = Field(
        description="Baptism holy spirit place", alias="baptismHolySpiritPlace"
    )
    baptism_pastor_name: Optional[str] = Field(description="Baptism pastor name", alias="baptismPastorName")
    baptism_denomination: Optional[str] = Field(description="Baptism denomination", alias="baptismDenomination")
    active_member_since: Optional[date] = Field(description="Active member since", alias="activeMemberSince")
    leaving_reason: Optional[serialized_enum_by_name(LeavingReasonType)] = Field(
        description="Leaving reason", alias="leavingReason"
    )
    leaving_reason_description: Optional[str] = Field(description="Leaving reason", alias="leavingReasonDescription")
    leaving_date: Optional[date] = Field(description="Leaving date", alias="leavingDate")
    acceptance_comment: Optional[str] = Field(description="Acceptance comment", alias="acceptanceComment")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class CreateMemberGeneralDataRequest(BaseModel):
    conversion_date: Optional[date] = Field(description="Conversion date", alias="conversionDate")
    conversion_place: Optional[str] = Field(description="Convertion place", alias="conversionPlace")
    baptism_date: Optional[date] = Field(description="Baptism date", alias="baptismDate")
    baptism_place: Optional[str] = Field(description="Baptism place", alias="baptismPlace")
    baptism_holy_spirit_date: Optional[date] = Field(
        description="Baptism holy spirit date", alias="baptismHolySpiritDate"
    )
    baptism_holy_spirit_place: Optional[str] = Field(
        description="Baptism holy spirit place", alias="baptismHolySpiritPlace"
    )
    baptism_pastor_name: Optional[str] = Field(description="Baptism pastor name", alias="baptismPastorName")
    baptism_denomination: Optional[str] = Field(description="Baptism denomination", alias="baptismDenomination")
    active_member_since: Optional[date] = Field(description="Active member since", alias="activeMemberSince")
    leaving_reason: Optional[serialized_enum_by_name(LeavingReasonType)] = Field(
        description="Leaving reason", alias="leavingReason"
    )
    leaving_reason_description: Optional[str] = Field(description="Leaving reason", alias="leavingReasonDescription")
    leaving_date: Optional[date] = Field(description="Leaving date", alias="leavingDate")
    acceptance_comment: Optional[str] = Field(description="Acceptance comment", alias="acceptanceComment")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class UpdateMemberGeneralDataRequest(CreateMemberGeneralDataRequest):
    id: int = Field(description="Member general data ID", gt=0)

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
