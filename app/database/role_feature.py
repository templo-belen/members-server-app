from sqlalchemy import Boolean, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database.connection import Base
from app.database.feature import Feature


class RoleFeature(Base):
    __tablename__ = "role_features"

    role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True, nullable=False)
    feature_id = Column(Integer, ForeignKey("features.id"), primary_key=True, nullable=False)
    enabled = Column(Boolean, nullable=False, default=True)

    feature = relationship(Feature)
