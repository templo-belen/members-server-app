from sqlalchemy.orm import Session

from app.database.reports import ReportColumns
from app.models.reports import ReportColumn


class ReportsService:
    def __init__(self):
        pass

    def get_columns(self, db: Session) -> list[ReportColumn]:
        db_columns = db.query(ReportColumns).all()
        return list(
            map(
                lambda obj: ReportColumn(id=obj.id, group_name=obj.group_name, column_name=obj.readable_column_name),
                db_columns,
            )
        )
