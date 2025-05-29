from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict

from app.models import MaritalStatusType, HousingType


class FamilyDataResponse(BaseModel):
    member_id: int = Field(description="Member ID", alias="memberId")

    marital_status: Optional[MaritalStatusType] = Field(description="Marital status", alias="maritalStatus")
    fathers_name: Optional[str] = Field(description="Father's name", alias="fathersName")
    mothers_name: Optional[str] = Field(description="Mother's name", alias="mothersName")
    spouse_name: Optional[str] = Field(description="Spouse's name", alias="spouseName")
    spouse_occupation: Optional[str] = Field(description="Spouse's occupation", alias="spouseOccupation")
    marriage_registration_number: Optional[str] = Field(description="Marriage registration number", alias="marriageRegistrationNumber")
    housing: Optional[HousingType] = Field(description="Housing type", alias="housingType")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )

class MemberChildrenDataResponse(BaseModel):
    member_id: int = Field(description="Member ID", alias="memberId")
    child_name: str = Field(description="Child name", alias="childName")
    child_occupation: Optional[str] = Field(description="Child occupation", alias="childOccupation")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )

class MemberFamilyDataResponse(BaseModel):
    family_data: Optional[FamilyDataResponse] = Field(description="Member family data", alias="familyData")
    children_data_list: List[MemberChildrenDataResponse]  = Field(description="Member children data list", alias="childrenDataList")

    model_config = ConfigDict(
        populate_by_name=True
    )
