from sqlalchemy.orm import Session

from app.models.member_dew import MembersDEW, MembersDEWInformation


class MembersDEWService:
    def __init__(self):
        pass

    def find_by_id(self, member_id, db: Session) -> MembersDEWInformation | None:
        member_dew = db.query(MembersDEW).filter(MembersDEW.member_id == member_id).first()
        if not member_dew:
            return None
        return MembersDEWInformation.from_orm(member_dew)
