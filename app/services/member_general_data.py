from sqlalchemy.orm import Session

from app.models.member_general_data import MembersGeneralDataInformation, MembersGeneralData


class MembersGeneralDataService:
    def __init__(self):
        pass

    def find_by_id(self, id, db: Session) -> MembersGeneralDataInformation | None:
        member = db.query(MembersGeneralData).filter(MembersGeneralData.member_id == id).first()
        if not member:
            return None
        return MembersGeneralDataInformation.from_orm(member)
