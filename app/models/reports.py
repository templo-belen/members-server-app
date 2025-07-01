from pydantic import BaseModel


class ReportColumn(BaseModel):
    id: int
    group_name: str
    column_name: str
