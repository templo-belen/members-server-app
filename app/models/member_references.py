from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class MembersReferenceElement(BaseModel):
    id: int = Field(description="Member reference DB id")
    member_id: int = Field(description="Member ID", alias="memberId")

    total_time: Optional[int] = Field(description="Total time reference", alias="totalTime")
    church_name: Optional[str] = Field(description="Reference church name", alias="churchName")
    main_pastor_name: Optional[str] = Field(description="Reference main pastor name", alias="mainPastorName")
    leaving_reason: Optional[str] = Field(description="Leaving reason", alias="leavingReason")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class MemberReferenceResponse(BaseModel):
    references: Optional[List[MembersReferenceElement]] = Field(
        default=None,
        description="Member's reference list",
    )
    reasons_for_congregating: Optional[str] = Field(
        default=None, description="Reason why the member congregates", alias="reasonsForCongregating"
    )

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class CreateMemberReferenceRequest(BaseModel):
    total_time: Optional[int] = Field(description="Total time reference", alias="totalTime")
    church_name: Optional[str] = Field(description="Reference church name", alias="churchName")
    main_pastor_name: Optional[str] = Field(description="Reference main pastor name", alias="mainPastorName")
    leaving_reason: Optional[str] = Field(description="Leaving reason", alias="leavingReason")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class UpdateMemberReferenceRequest(CreateMemberReferenceRequest):
    id: int = Field(description="Member reference ID", gt=0)

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
