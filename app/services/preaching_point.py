from sqlalchemy.orm import Session

from app.models.preaching_point import PreachingPointInformation

from app.database.preaching_point import PreachingPoint


class PreachingPointService:
    def __init__(self):
        pass

    def get_all(self, db: Session) -> list[PreachingPointInformation]:
        preaching_points = db.query(PreachingPoint).filter(PreachingPoint.status != 'I')
        return [PreachingPointInformation.from_orm(pp) for pp in preaching_points]
