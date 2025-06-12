from sqlalchemy.orm import Session

from app.database import Member, MembersGeneralData
from app.middlewares import current_user_ctx
from app.models import (
    CreateMemberGeneralDataRequest,
    MemberGeneralDataResponse,
    UpdateMemberGeneralDataRequest,
)
from app.services import ConflictException, NotFoundException
from app.services.pydantic_tools import apply_updates_from_pydantic


class MembersGeneralDataService:
    def __init__(self):
        pass

    def find_by_member_id(self, member_id: int, db: Session) -> MemberGeneralDataResponse | None:
        member = db.query(MembersGeneralData).filter(MembersGeneralData.member_id == member_id).first()
        if not member:
            return None
        return MemberGeneralDataResponse.model_validate(member)

    def create_member_general_data(
        self, member_id: int, new_member_general_data: CreateMemberGeneralDataRequest, db: Session
    ) -> MemberGeneralDataResponse:
        member = db.query(Member).filter(Member.id == member_id).first()
        if not member:
            raise NotFoundException(f"El miembro con id {member_id} no existe.")

        self.validate_member_general_data(member_id, db)

        db_member_general_data = MembersGeneralData(**new_member_general_data.model_dump(exclude_unset=True))
        db_member_general_data.member_id = member_id
        db.add(db_member_general_data)

        member.updated_by = current_user_ctx.get().username
        db.commit()
        db.refresh(db_member_general_data)
        db.refresh(member)
        return MemberGeneralDataResponse.model_validate(db_member_general_data)

    def update_member_general_data(
        self, member_id: int, general_data: UpdateMemberGeneralDataRequest, db: Session
    ) -> MemberGeneralDataResponse:
        member_to_update = db.query(Member).filter(Member.id == member_id).first()
        if not member_to_update:
            raise NotFoundException(f"El miembro con id {member_id} no existe.")

        general_data_to_update = (
            db.query(MembersGeneralData)
            .filter(MembersGeneralData.id == general_data.id, MembersGeneralData.member_id == member_id)
            .first()
        )

        if not general_data_to_update:
            raise NotFoundException(
                f"Los datos generales con id {general_data.id} del miembro con id {member_id} no existen."
            )

        apply_updates_from_pydantic(general_data_to_update, general_data)

        member_to_update.updated_by = current_user_ctx.get().username
        db.commit()
        db.refresh(general_data_to_update)
        db.refresh(member_to_update)

        return MemberGeneralDataResponse.model_validate(general_data_to_update)

    def validate_member_general_data(self, member_id: int, db: Session):
        member_general_data = self.find_by_member_id(member_id, db)
        if member_general_data:
            raise ConflictException(f"El miembro con id {member_id} ya tiene datos generales")
