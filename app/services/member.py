from sqlalchemy.orm import Session

from app.models.member import Member, MemberBasicInformation, MemberPersonalInformation


class MemberService:
    def __init__(self):
        pass

    def get_all(self, db: Session) -> list[MemberBasicInformation]:
        members = db.query(Member).all()
        return [MemberBasicInformation.from_orm(m) for m in members]
    
    def find_by_id(self, id, db: Session) -> MemberPersonalInformation | None:
        member = db.query(Member).filter(Member.id == id).first()
        if not member:
            return None
        return MemberPersonalInformation.from_orm(member)
