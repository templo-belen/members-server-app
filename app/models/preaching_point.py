from sqlalchemy import String, Column, Integer

from app.models.base_table_model import BaseTableModel


class PreachingPoint(BaseTableModel):
    __tablename__ = "preaching_point"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
