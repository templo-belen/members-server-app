from sqlalchemy import Boolean, Column, Integer, Text

from app.database.connection import Base


class Feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True)
    code = Column(Text, unique=True, index=True, nullable=False)
    name = Column(Text)
    enabled = Column(Boolean, default=True, nullable=False)
