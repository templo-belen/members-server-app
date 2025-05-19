from sqlalchemy.orm import Session

from app.database import MembersGeneralData
from app.models import MemberGeneralDataResponse


class MembersGeneralDataService:
    def __init__(self):
        pass

    def find_by_id(self, id, db: Session) -> MemberGeneralDataResponse | None:
        member = db.query(MembersGeneralData).filter(MembersGeneralData.member_id == id).first()
        if not member:
            return None
        return MemberGeneralDataResponse.from_orm(member)
