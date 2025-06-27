from sqlalchemy.orm import Session

from app.database import Member, MembersReference
from app.middlewares import current_user_ctx
from app.models import MemberReferenceResponse, MembersReferenceElement
from app.models.member_references import UpdateMemberReferenceRequest
from app.services.exception import NotFoundException
from app.services.pydantic_tools import apply_updates_from_pydantic


class MembersReferenceService:
    def __init__(self):
        pass

    def find_by_member_id(self, member_id: int, db: Session) -> MemberReferenceResponse | None:
        member_data = db.query(Member.id, Member.reasons_for_congregating).filter(Member.id == member_id).first()

        reasons_for_congregating = None
        if member_data:
            reasons_for_congregating = member_data.reasons_for_congregating

        # Getting references
        references = db.query(MembersReference).filter(MembersReference.member_id == member_id).all()

        references_pydantic = []
        if references:
            references_pydantic = [MembersReferenceElement.model_validate(ref) for ref in references]

        if not reasons_for_congregating and not references_pydantic:
            return None

        return MemberReferenceResponse(
            references=references_pydantic, reasons_for_congregating=reasons_for_congregating
        )
    def update_member_reference(
        self,
        member_id: int,
        reference_data: UpdateMemberReferenceRequest,
        db: Session
    ) -> MembersReferenceElement:
        member_to_update = db.query(Member).filter(Member.id == member_id).first()
        if not member_to_update:
            raise NotFoundException(
                f"El miembro con id {member_id} no existe."
            )

        reference_to_update = (
            db.query(MembersReference)
            .filter(
                MembersReference.id == reference_data.id,
                MembersReference.member_id == member_id
            )
            .first()
        )
        if not reference_to_update:
            raise NotFoundException(
                f"Los datos de referencia con id {reference_data.id} del miembro "
                f"con id {member_id} no existen."
            )

        apply_updates_from_pydantic(reference_to_update, reference_data)

        member_to_update.updated_by = current_user_ctx.get().username
        db.commit()
        db.refresh(reference_to_update)
        db.refresh(member_to_update)
        return MembersReferenceElement.model_validate(reference_to_update)
