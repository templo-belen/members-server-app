from sqlalchemy.orm import Session

from app.database import Member, MembersDEW
from app.middlewares import current_user_ctx
from app.models import MembersDEWResponse, UpdateMemberDEWRequest
from app.models.member_dew import CreateMemberDEWRequest
from app.services import ConflictException, NotFoundException
from app.services.pydantic_tools import apply_updates_from_pydantic


class MembersDEWService:
    def __init__(self):
        pass

    def find_by_member_id(self, member_id, db: Session) -> MembersDEWResponse | None:
        member_dew = db.query(MembersDEW).filter(MembersDEW.member_id == member_id).first()
        if not member_dew:
            return None
        return MembersDEWResponse.model_validate(member_dew)

    def create_member_dew(self, member_id : int, new_dew: CreateMemberDEWRequest, db: Session) -> MembersDEWResponse:
        member = db.query(Member).filter(Member.id == member_id).first()
        if not member:
            raise NotFoundException(f'El miembro con id {member_id} no existe.')

        self.validate_member_dew(member_id, db)

        db_member_dew = MembersDEW(**new_dew.model_dump(exclude_unset=True))
        db_member_dew.member_id = member_id
        db.add(db_member_dew)

        member.updated_by = current_user_ctx.get().username
        db.commit()
        db.refresh(db_member_dew)
        db.refresh(member)
        return MembersDEWResponse.model_validate(db_member_dew)

    def update_member_dew(self, member_id : int, dew_data: UpdateMemberDEWRequest, db: Session) -> MembersDEWResponse:
        member_to_update = db.query(Member).filter(Member.id == member_id).first()
        if not member_to_update:
            raise NotFoundException(f'El miembro con id {member_id} no existe.')

        dew_to_update = (db.query(MembersDEW)
                         .filter(MembersDEW.id == dew_data.id, MembersDEW.member_id == member_id)
                         .first())

        if not dew_to_update:
            raise NotFoundException(f'Los datos dew con id {dew_data.id} del miembro con id {member_id} no existe.')

        apply_updates_from_pydantic(dew_to_update, dew_data)

        member_to_update.updated_by = current_user_ctx.get().username
        db.commit()
        db.refresh(dew_to_update)
        db.refresh(member_to_update)

        return MembersDEWResponse.model_validate(dew_to_update)

    def validate_member_dew(self, member_id: int, db: Session):
        member_dew = self.find_by_member_id(member_id, db)
        if member_dew:
            raise ConflictException(f'El miembro con id {member_id} ya tiene datos DEW')
