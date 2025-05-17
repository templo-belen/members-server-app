from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator, field_serializer

from app.models.enum_serializer import SerializedEnumByName
from app.models.enum_type import GenderType, RoleType, LeadershipType, CellLeadershipType, BloodType
from app.models.preaching_point import PreachingPointInformation

"""
This class makes it easier when loading zone pastor data as part of the member data.
"""
class MemberName(BaseModel):
    names: str
    surnames: str

    model_config = ConfigDict(from_attributes=True)

"""
This class makes it easier when loading zone pastor and the id data as part of the member data.
"""
class MemberBasicData(BaseModel):
    id: int
    names: str
    surnames: str

    model_config = ConfigDict(from_attributes=True)

class MemberListItemResponse(BaseModel):
    id: int = Field(description="User database identifier")
    id_number: str = Field(description="Member ID number", alias="idNumber")
    surnames: str = Field(description="Member surnames")
    names: str = Field(description="Member names")
    birthdate: Optional[datetime] = Field(description="Member birth date")
    birth_country: Optional[str] = Field(description="Member birth country", alias="birthCountry")
    residence_country: Optional[str] = Field(description="Member residence country", alias="residenceCountry")
    address: Optional[str] = Field(description="Member address")
    phone_number: Optional[str] = Field(description="Phone number", alias="phoneNumber")
    cellphone_number: Optional[str] = Field(description="Member cell phone number", alias="cellphoneNumber")
    email: Optional[str] = Field(description="Member email", examples=["templo.belen@mail.com"])
    occupation: Optional[str] = Field(description="Member occupation")
    zone_pastor: Optional[MemberName] = Field(description="Zone pastor names", alias="zonePastor")
    cell_leadership: CellLeadershipType = Field(description="Cell leadership", exclude=True)
    is_pastor: Optional[bool] = Field(None, description="Indicates if the member is pastor or not", alias="isPastor")
    is_cell_leader: Optional[bool] = Field(None, description="Indicates if the member is cell leader or not", alias="isCellLeader")
    role: RoleType = Field(description="Member current role", alias="currentRole")
    status: str = Field(description="Member current status")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )

    @model_validator(mode="after")
    def set_booleans(self):
        self.is_pastor = self.cell_leadership in {CellLeadershipType.pastor_zona,
                                                  CellLeadershipType.pastor_principal}
        self.is_cell_leader = self.cell_leadership in {CellLeadershipType.lider_celula}
        return self

    @field_serializer("zone_pastor")
    def serialize_zone_pastor(self, obj, _info):
        return f"{obj.names} {obj.surnames}" if obj else None

class MemberPersonalInformationResponse(BaseModel):
    id: int = Field(description="User database identifier")
    id_number: str = Field(description="Member ID number", alias="idNumber")
    surnames: str = Field(description="Member surnames")
    names: str = Field(description="Member names")
    birthdate: Optional[datetime] = Field(description="Member birth date")
    birth_country: Optional[str] = Field(description="Member birth country", alias="birthCountry")
    residence_country: Optional[str] = Field(description="Member residence country", alias="residenceCountry")
    address: Optional[str] = Field(description="Member address")
    phone_number: Optional[str] = Field(description="Phone number", alias="phoneNumber")
    cellphone_number: Optional[str] = Field(description="Member cell phone number", alias="cellphoneNumber")
    email: Optional[str] = Field(description="Member email", examples=["templo.belen@mail.com"])
    military_service: Optional[str] = Field(description="Military service number", alias="militaryService")
    studies_completed: Optional[str] = Field(description="Completed studies description", alias="studiesCompleted")
    degree_obtained: Optional[str] = Field(description="Obtained degree description", alias="degreeObtained")
    other_studies: Optional[str] = Field(description="Other studies description", alias="otherStudies")
    company: Optional[str] = Field(description="Company name", alias="company")
    occupation: Optional[str] = Field(description="Member occupation")
    eps: Optional[str] = Field(description="Member eps")
    rh: Optional[SerializedEnumByName(BloodType)] = Field(description="Member rh")
    gender: Optional[SerializedEnumByName(GenderType)] = Field(description="Gender type")

    preaching_point: Optional[PreachingPointInformation] = Field(description="Preaching point", alias="preachingPoint")
    role: SerializedEnumByName(RoleType) = Field(description="Member current role", alias="currentRole")
    commitment_date: Optional[datetime] = Field(description="Commitment date", alias="commitmentDate")
    cell_leadership: SerializedEnumByName(CellLeadershipType) = Field(description="Cell leadership", alias="cellLeadership")
    zone_pastor: Optional[MemberBasicData] = Field(description="Member zone pastor data", alias="zonePastor")
    leadership: SerializedEnumByName(LeadershipType) = Field(description="Leadership")
    status: str = Field(description="Member current status")

    created_at: datetime = Field(description="Member creation date", alias="createdAt")
    created_by: str = Field(description="Member created by", alias="createdBy")
    updated_at: datetime = Field(description="Member update date", alias="updatedAt")
    updated_by: str = Field(description="Member updated by", alias="updatedBy")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )
