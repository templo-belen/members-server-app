from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator, field_serializer
from sqlalchemy import Column, String, TIMESTAMP, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.models.EnumType import GenderType, RoleType, LeadershipType, CellLeadershipType
from app.models.base_table_model import BaseTableModel
from app.models.preaching_point import PreachingPoint


class Member(BaseTableModel):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)

    id_number = Column(String(50), nullable=False, unique=True)
    surnames = Column(String(100), nullable=False)
    names = Column(String(100), nullable=False)
    birthdate = Column(TIMESTAMP)
    birth_country = Column(String(50))
    residence_country = Column(String(50))
    address = Column(String(100))
    phone_number = Column(String(20))
    cellphone_number = Column(String(20))
    email = Column(String(100))
    military_service = Column(String(20))
    studies_completed = Column(String(100))
    degree_obtained = Column(String(100))
    other_studies = Column(String(100))
    company = Column(String(100))
    occupation = Column(String(100))
    eps = Column(String(50))
    rh = Column(String(5))
    gender = Column(Enum(GenderType, name="gender_type", native_enum=True), nullable=True)

    role = Column(Enum(RoleType, name="role_type", native_enum=False), nullable=False)
    zone_pastor_id = Column(Integer, ForeignKey("members.id"), nullable=True)
    cell_leadership = Column(Enum(CellLeadershipType, name="cell_leadership_type", native_enum=True), nullable=False)
    leadership = Column(Enum(LeadershipType, name="leadership_type", native_enum=True), nullable=False)
    preaching_point_id = Column(Integer, ForeignKey("preaching_point.id"))

    #Relationships
    preaching_point = relationship(PreachingPoint)
    zone_pastor = relationship("Member", remote_side=[id], backref="zone_members", lazy="select")


# Pydantic models

"""
This class makes it easier when loading zone pastor data as part of the member data.
"""
class MemberName(BaseModel):
    names: str
    surnames: str

    model_config = ConfigDict(from_attributes=True)

class MemberBasicInformation(BaseModel):
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
    role: Optional[str] = Field(description="Member current role", alias="currentRole")
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
