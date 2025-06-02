from sqlalchemy.orm import Session

from app.database import MembersGeneralData, Member
from app.middlewares import current_user_ctx
from app.models import MemberGeneralDataResponse, CreateMemberGeneralDataRequest
from app.services import NotFoundException, ConflictException


class MembersGeneralDataService:
    def __init__(self):
        pass

    def find_by_id(self, member_id : int, db: Session) -> MemberGeneralDataResponse | None:
        member = db.query(MembersGeneralData).filter(MembersGeneralData.member_id == member_id).first()
        if not member:
            return None
        return MemberGeneralDataResponse.from_orm(member)

    def create_member_general_data(self, new_member_general_data: CreateMemberGeneralDataRequest, db: Session) -> MemberGeneralDataResponse:
        member = db.query(Member).filter(Member.id == new_member_general_data.member_id).first()
        if not member:
            raise NotFoundException(f'El miembro con id {member.id} no existe.')

        self.validate_member_general_data(new_member_general_data.member_id, db)

        db_member_general_data = MembersGeneralData(**new_member_general_data.model_dump(exclude_unset=True))
        db.add(db_member_general_data)

        member.updated_by = current_user_ctx.get().username
        db.commit()
        db.refresh(db_member_general_data)
        db.refresh(member)
        return MemberGeneralDataResponse.model_validate(db_member_general_data)

    def validate_member_general_data(self, member_id: int, db: Session):
        member_general_data = self.find_by_id(member_id , db)
        if member_general_data:
            raise ConflictException(f'El miembro con id {member_id} ya tiene datos generales')
