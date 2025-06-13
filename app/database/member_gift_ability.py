from sqlalchemy import Column, Enum, ForeignKey, Integer, String

from app.database.connection import Base
from app.models.enum_type import GiftAbilityType


class MemberGiftAbility(Base):
    __tablename__ = "members_gift_ability"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    type = Column(Enum(GiftAbilityType, name="gift_ability_type", native_enum=False), nullable=False)

    member_id = Column(Integer, ForeignKey("members.id"), unique=False, nullable=False)
