from sqlalchemy.orm import Session

from app.database import Member
from app.middlewares import current_user_ctx
from app.models import (
    CellLeadershipType,
    CreateMemberRequest,
    MemberBasicData,
    MemberListItemResponse,
    MemberPersonalInformationResponse,
    UpdateMemberRequest,
)
from app.services.exception import LogicConstraintViolationException, NotFoundException
from app.services.pydantic_tools import apply_updates_from_pydantic


class MemberService:
    def __init__(self):
        pass

    def get_all(self, db: Session) -> list[MemberListItemResponse]:
        members = db.query(Member).all()
        return [MemberListItemResponse.from_orm(m) for m in members]

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
        members = (
            db.query(Member.id, Member.names, Member.surnames).filter(Member.cell_leadership == cell_leadership).all()
        )
        if not members:
            return None
        return [MemberBasicData.model_validate(member) for member in members]

    def create_member(self, new_member: CreateMemberRequest, db: Session) -> MemberPersonalInformationResponse:
        current_user = current_user_ctx.get()
        db_member = Member(
            **new_member.model_dump(exclude_unset=True),
            created_by=current_user.username,
            updated_by=current_user.username,
        )

        self.validate_zone_pastor(new_member.zone_pastor_id, db)

        db.add(db_member)
        db.commit()
        db.refresh(db_member)
        return MemberPersonalInformationResponse.model_validate(db_member)

    def update_member(self, member: UpdateMemberRequest, db: Session) -> MemberPersonalInformationResponse:
        member_to_update = db.query(Member).filter(Member.id == member.id).first()
        if not member_to_update:
            raise NotFoundException(f"El miembro con id {member.id} no existe.")

        self.validate_zone_pastor(member.zone_pastor_id, db)

        apply_updates_from_pydantic(member_to_update, member)

        member_to_update.updated_by = current_user_ctx.get().username
        db.commit()
        db.refresh(member_to_update)

        return MemberPersonalInformationResponse.model_validate(member_to_update)

    def validate_zone_pastor(self, zone_pastor_id: int, db: Session):
        """
        Validates that the selected member is an existing zone pastor.
        :param self:
        :param zone_pastor_id: Member id
        :param db: database connection
        :return:
        """
        if not zone_pastor_id:
            return

        zone_pastor = self.find_by_id(zone_pastor_id, db)

        if not zone_pastor:
            raise LogicConstraintViolationException(f"El pastor con id {zone_pastor_id} no existe")

        pastor_cell_leadership_types = [CellLeadershipType.pastor_principal, CellLeadershipType.pastor_zona]
        if zone_pastor.cell_leadership and zone_pastor.cell_leadership not in pastor_cell_leadership_types:
            raise LogicConstraintViolationException("El pastor de zona proporcionado no tiene el rol de pastor.")
