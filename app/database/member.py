from sqlalchemy import Column, String, TIMESTAMP, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database.base_table_model import BaseTableModel
from app.database.preaching_point import PreachingPoint
from app.models.enum_type import GenderType, RoleType, LeadershipType, CellLeadershipType, BloodType


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
    rh = Column(Enum(BloodType, name="blood_type", native_enum=False), nullable=True)
    gender = Column(Enum(GenderType, name="gender_type", native_enum=False), nullable=True)

    role = Column(Enum(RoleType, name="role_type", native_enum=False), nullable=False)
    zone_pastor_id = Column(Integer, ForeignKey("members.id"), nullable=True)
    commitment_date = Column(TIMESTAMP)
    cell_leadership = Column(Enum(CellLeadershipType, name="cell_leadership_type", native_enum=False), nullable=False)
    leadership = Column(Enum(LeadershipType, name="leadership_type", native_enum=False), nullable=False)
    preaching_point_id = Column(Integer, ForeignKey("preaching_point.id"))
    reasons_for_congregating = Column(String(250))

    #Relationships
    preaching_point = relationship(PreachingPoint)
    zone_pastor = relationship("Member", remote_side=[id], backref="zone_members", lazy="select")
