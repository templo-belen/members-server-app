from sqlalchemy.orm import Session

from app.database import MembersDEW, Member
from app.middlewares import current_user_ctx
from app.models import MembersDEWResponse
from app.models.member_dew import CreateMemberDEWRequest
from app.services import NotFoundException, ConflictException


class MembersDEWService:
    def __init__(self):
        pass

    def find_by_member_id(self, member_id, db: Session) -> MembersDEWResponse | None:
        member_dew = db.query(MembersDEW).filter(MembersDEW.member_id == member_id).first()
        if not member_dew:
            return None
        return MembersDEWResponse.from_orm(member_dew)

    def create_member_dew(self, new_dew: CreateMemberDEWRequest, db: Session) -> MembersDEWResponse:
        member = db.query(Member).filter(Member.id == new_dew.member_id).first()
        if not member:
            raise NotFoundException(f'El miembro con id {new_dew.member_id} no existe.')

        self.validate_member_dew(new_dew.member_id, db)

        db_member_dew = MembersDEW(**new_dew.model_dump(exclude_unset=True))
        db.add(db_member_dew)

        member.updated_by = current_user_ctx.get().username
        db.commit()
        db.refresh(db_member_dew)
        db.refresh(member)
        return MembersDEWResponse.model_validate(db_member_dew)

    def validate_member_dew(self, member_id: int, db: Session):
        member_dew = self.find_by_member_id(member_id, db)
        if member_dew:
            raise ConflictException(f'El miembro con id {member_id} ya tiene datos DEW')
