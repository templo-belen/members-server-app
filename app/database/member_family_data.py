from sqlalchemy import Column, Enum, ForeignKey, Integer, String

from app.database.connection import Base
from app.models import HousingType, MaritalStatusType


class MemberFamilyData(Base):
    __tablename__ = "members_family_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    marital_status = Column(Enum(MaritalStatusType, name="marital_status_type", native_enum=False),
                            nullable=True)
    fathers_name = Column(String(150))
    mothers_name = Column(String(150))
    spouse_name = Column(String(150))
    spouse_occupation = Column(String(150))
    marriage_registration_number = Column(String(150))
    housing = Column(Enum(HousingType, name="housing_type", native_enum=False), nullable=True)

    member_id = Column(Integer, ForeignKey('members.id'), unique=True, nullable=False)
