from sqlalchemy.orm import Session

from app.models.preaching_point import PreachingPointInformation, PreachingPoint


class PreachingPointService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[PreachingPointInformation]:
        preaching_points = self.db.query(PreachingPoint).filter(PreachingPoint.status != 'I')
        return [PreachingPointInformation.from_orm(pp) for pp in preaching_points]
