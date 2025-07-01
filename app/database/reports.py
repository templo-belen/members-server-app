from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class ReportColumns(Base):
    __tablename__ = "available_columns"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    column_name: Mapped[str] = mapped_column(String(50), nullable=False)
    table_name: Mapped[str] = mapped_column(String(50), nullable=False)
    group_name: Mapped[str] = mapped_column(String(250), nullable=False)
    readable_column_name: Mapped[str] = mapped_column(String(250), nullable=False)
