from sqlalchemy.orm import Session

from app.database import Member, MembersReference
from app.models import MemberReferenceResponse, MembersReferenceElement


class MembersReferenceService:
    def __init__(self):
        pass

    def find_by_member_id(self, member_id: int, db: Session) -> MemberReferenceResponse | None:
        member_data = db.query(Member.id, Member.reasons_for_congregating) \
            .filter(Member.id == member_id) \
            .first()

        reasons_for_congregating = None
        if member_data:
            reasons_for_congregating = member_data.reasons_for_congregating

        # Getting references
        references = db.query(MembersReference) \
            .filter(MembersReference.member_id == member_id) \
            .all()

        references_pydantic = []
        if references:
            references_pydantic = [MembersReferenceElement.model_validate(ref) for ref in references]

        if not reasons_for_congregating and not references_pydantic:
            return None

        return MemberReferenceResponse(
            references=references_pydantic,
            reasons_for_congregating=reasons_for_congregating
        )
