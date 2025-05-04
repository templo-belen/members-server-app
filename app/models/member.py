from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import Integer, Column, String, TIMESTAMP, Boolean

from app.models.base_table_model import BaseTableModel


class Member(BaseTableModel):
    __tablename__ = "members"

    id_number = Column(String(50), nullable=False, unique=True)
    surnames = Column(String(100), nullable=False)
    names = Column(String(100), nullable=False)
    birthdate = Column(TIMESTAMP)
    birth_country = Column(String(100))
    residence_country = Column(String(100))
    address = Column(String(200))
    phone_number = Column(String(20))
    cellphone_number = Column(String(20))
    email = Column(String(150))
    military_service = Column(String(50))
    studies_completed = Column(String(100))
    degree_obtained = Column(String(100))
    other_studies = Column(String(100))
    company = Column(String(100))
    occupation = Column(String(100))
    eps = Column(String(50))
    rh = Column(String(5))
    gender = Column(String(10))
    leadership = Column(String(100))
    zone_pastor = Column(String(100))
    current_role = Column(String(100))

    is_pastor = Column(Boolean, nullable=False, default=False)
    is_cell_leader = Column(Boolean, nullable=False, default=False)

# Pydantic models

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
    cellphone_number: Optional[str] = Field(description="Member cell phone number", alias = "cellphoneNumber")
    email: Optional[str] = Field(description="Member email", examples=["templo.belen@mail.com"])
    occupation: Optional[str] = Field(description="Member occupation")
    zone_pastor: Optional[str] = Field(description="Member zone pastor", alias="zonePastor")
    is_pastor: bool = Field(description="Indicates if the member is pastor or not", alias="isPastor")
    is_cell_leader: bool = Field(description="Indicates if the member is cell leader or not", alias="isCellLeader")
    current_role: Optional[str] = Field(description="Member current role", alias="currentRole")
    status: str = Field(description="Member current status")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )
