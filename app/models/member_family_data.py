from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from app.models import HousingType, MaritalStatusType
from app.models.enum_serializer import serialized_enum_by_name


class FamilyDataResponse(BaseModel):
    id: int = Field(description="Member family data information DB id")
    member_id: int = Field(description="Member ID", alias="memberId")

    marital_status: Optional[serialized_enum_by_name(MaritalStatusType)] = Field(
        description="Marital status", alias="maritalStatus"
    )
    fathers_name: Optional[str] = Field(description="Father's name", alias="fathersName")
    mothers_name: Optional[str] = Field(description="Mother's name", alias="mothersName")
    spouse_name: Optional[str] = Field(description="Spouse's name", alias="spouseName")
    spouse_occupation: Optional[str] = Field(description="Spouse's occupation", alias="spouseOccupation")
    marriage_registration_number: Optional[str] = Field(
        description="Marriage registration number", alias="marriageRegistrationNumber"
    )
    housing: Optional[serialized_enum_by_name(HousingType)] = Field(description="Housing type", alias="housingType")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class MemberChildrenDataResponse(BaseModel):
    id: int = Field(description="Member children DB id")
    member_id: int = Field(description="Member ID", alias="memberId")
    child_name: str = Field(description="Child name", alias="childName")
    child_occupation: Optional[str] = Field(description="Child occupation", alias="childOccupation")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class MemberFamilyDataResponse(BaseModel):
    family_data: Optional[FamilyDataResponse] = Field(description="Member family data", alias="familyData")
    children_data_list: List[MemberChildrenDataResponse] = Field(
        description="Member children data list", alias="childrenDataList"
    )

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class CreateMemberChildrenDataRequest(BaseModel):
    child_name: str = Field(description="Child name", alias="childName")
    child_occupation: Optional[str] = Field(description="Child occupation", alias="childOccupation")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class CreateFamilyDataRequest(BaseModel):
    marital_status: Optional[serialized_enum_by_name(MaritalStatusType)] = Field(
        description="Marital status", alias="maritalStatus"
    )
    fathers_name: Optional[str] = Field(description="Father's name", alias="fathersName")
    mothers_name: Optional[str] = Field(description="Mother's name", alias="mothersName")
    spouse_name: Optional[str] = Field(description="Spouse's name", alias="spouseName")
    spouse_occupation: Optional[str] = Field(description="Spouse's occupation", alias="spouseOccupation")
    marriage_registration_number: Optional[str] = Field(
        description="Marriage registration number", alias="marriageRegistrationNumber"
    )
    housing: Optional[serialized_enum_by_name(HousingType)] = Field(description="Housing type", alias="housingType")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class CreateMemberFamilyDataRequest(BaseModel):
    family_data: Optional[CreateFamilyDataRequest] = Field(description="Member family data", alias="familyData")
    children_data_list: Optional[List[CreateMemberChildrenDataRequest]] = Field(
        description="Member children data list", alias="childrenDataList"
    )

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
