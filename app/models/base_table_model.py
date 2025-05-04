from sqlalchemy import Column, TIMESTAMP, String, Integer

from app.database import Base

class BaseTableModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    created_by = Column(String(50))
    updated_by = Column(String(50))
    status = Column(String(1), nullable=False, default='A')
