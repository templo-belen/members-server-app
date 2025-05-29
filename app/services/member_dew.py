from app.database import MembersDEW, Session
from app.models import MembersDEWResponse


class MembersDEWService:
    def __init__(self):
        pass

    def find_by_member_id(self, member_id, db: Session) -> MembersDEWResponse | None:
        member_dew = db.query(MembersDEW).filter(MembersDEW.member_id == member_id).first()
        if not member_dew:
            return None
        return MembersDEWResponse.from_orm(member_dew)
