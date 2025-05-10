from sqlalchemy.orm import Session

from app.models.member import Member, MemberBasicInformation, MemberPersonalInformation


class MemberService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[MemberBasicInformation]:
        members = self.db.query(Member).all()
        return [MemberBasicInformation.from_orm(m) for m in members]
    
    def find_by_id(self, id) -> MemberPersonalInformation | None:
        member = self.db.query(Member).filter(Member.id == id).first()
        if not member:
            return None
        return MemberPersonalInformation.from_orm(member)
