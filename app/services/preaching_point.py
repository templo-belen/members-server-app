from sqlalchemy.orm import Session

from app.database import PreachingPoint
from app.models import PreachingPointInformation


class PreachingPointService:
    def __init__(self):
        pass

    def get_all(self, db: Session) -> list[PreachingPointInformation]:
        preaching_points = db.query(PreachingPoint).filter(PreachingPoint.status != 'I')
        return [PreachingPointInformation.from_orm(pp) for pp in preaching_points]
