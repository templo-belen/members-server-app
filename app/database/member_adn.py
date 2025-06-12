from sqlalchemy import Column, ForeignKey, Integer, String

from app.database.connection import Base


class MemberADN(Base):
    __tablename__ = "members_adn"

    id = Column(Integer, primary_key=True, autoincrement=True)
    passion = Column(String(300))
    mission = Column(String(300))
    personal_prophecies = Column(String(300))
    personal_values = Column(String(300))
    one_year_plans = Column(String(300))
    two_year_plans = Column(String(300))
    five_year_plans = Column(String(300))
    strengths = Column(String(300))
    weaknesses = Column(String(300))
    improvement_areas = Column(String(300))
    mentor = Column(String(250))
    mentor_frequency = Column(String(50))
    mentee = Column(String(250))
    mentee_frequency = Column(String(50))

    member_id = Column(Integer, ForeignKey('members.id'), unique=True, nullable=False)
