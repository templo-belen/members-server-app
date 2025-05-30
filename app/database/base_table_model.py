from sqlalchemy import Column, TIMESTAMP, String, text, func

from app.database.connection import Base


class BaseTableModel(Base):
    __abstract__ = True

    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=func.now())
    created_by = Column(String(50), nullable=False)
    updated_by = Column(String(50), nullable=False)
    status = Column(String(1), nullable=False, default='A')
