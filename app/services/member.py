from app.database import Member, Session
from app.models import (
    CreateMemberRequest,
    MemberListItemResponse,
    MemberPersonalInformationResponse,
    MemberBasicData,
)


class MemberService:
    def __init__(self):
        pass

    def get_all(self, db: Session) -> list[MemberListItemResponse]:
        members = db.query(Member).all()
        return [MemberListItemResponse.from_orm(m) for m in members]
    
    def create_member(new_member: CreateMemberRequest, db: Session) -> MemberPersonalInformationResponse:
        db_member = Member(**new_member.model_dump(exclude_unset=True))
        db.add(db_member)
        db.commit()
        db.refresh(db_member)
        return MemberPersonalInformationResponse.model_validate(db_member)
    
    def find_by_id(self, id, db: Session) -> MemberPersonalInformationResponse | None:
        member = db.query(Member).filter(Member.id == id).first()
        if not member:
            return None
        return MemberPersonalInformationResponse.model_validate(member)

    def get_all_by_cell_leadership(self, cell_leadership, db: Session) -> list[MemberBasicData] | None:
        """
        Returns all the members with a specific cell leadership
        :param cell_leadership:
        :param db:
        :return:
        """
        members = (db.query(Member.id, Member.names, Member.surnames)
                   .filter(Member.cell_leadership == cell_leadership, Member.status == 'A').all())
        if not members:
            return None
        return [MemberBasicData.model_validate(member) for member in members]
