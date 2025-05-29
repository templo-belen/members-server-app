from sqlalchemy.orm import Session


from app.database import Member
from app.models import (
    CellLeadershipType,
    CreateMemberRequest,
    MemberListItemResponse,
    MemberPersonalInformationResponse,
    MemberBasicData,
)
from app.middlewares import current_user_ctx
from app.services.exception import LogicConstraintViolationException


class MemberService:
    def __init__(self):
        pass

    def get_all(self, db: Session) -> list[MemberListItemResponse]:
        members = db.query(Member).all()
        return [MemberListItemResponse.from_orm(m) for m in members]
    
    def create_member(self, new_member: CreateMemberRequest, db: Session) -> MemberPersonalInformationResponse:
        current_user = current_user_ctx.get()
        db_member = Member(**new_member.model_dump(exclude_unset=True),
                           created_by=current_user.username,
                           updated_by=current_user.username)

        zone_pastor = self.find_by_id(new_member.zone_pastor_id, db)
        pastor_cell_leadership_types = [CellLeadershipType.pastor_principal, CellLeadershipType.pastor_zona]
        if (
            zone_pastor
            and zone_pastor.cell_leadership
            and zone_pastor.cell_leadership not in pastor_cell_leadership_types
        ):
            raise LogicConstraintViolationException('El pastor de zona proporcionado no tiene el rol de pastor.')

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
        :param cell_leadership: Cell leadership from CellLeadershipType
        :param db: Database connection
        :return:
        """
        members = (db.query(Member.id, Member.names, Member.surnames)
                   .filter(Member.cell_leadership == cell_leadership).all())
        if not members:
            return None
        return [MemberBasicData.model_validate(member) for member in members]
