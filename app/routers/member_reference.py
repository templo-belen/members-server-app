from typing import Optional

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import (
    MemberReferenceResponse,
)
from app.services import (
    AuthService,
    MembersReferenceService,
)


class MemberReferenceRouter:
    def __init__(self,
                 member_reference_service: MembersReferenceService,
                 auth_service: AuthService
                 ):
        self.auth_service = auth_service
        self.member_reference_service = member_reference_service

        self.router = APIRouter(prefix="/members/{member_id}/references", tags=["member-reference"])
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):

        @self.router.get(
            "/",
            response_model=Optional[MemberReferenceResponse],
            dependencies=[Depends(self.auth_service.require_role(["admin", "pastor", "readonly"]))]
        )
        def find_references_by_member_id(member_id : int, db: Session = Depends(get_db)):
            member_references = self.member_reference_service.find_by_member_id(member_id, db)
            if not member_references:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member_references
