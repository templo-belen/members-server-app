from sqlalchemy.orm import Session

from app.models.member import Member, MemberBasicInformation


class MemberService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[MemberBasicInformation]:
        members = self.db.query(Member).all()
        return [MemberBasicInformation.from_orm(m) for m in members]
