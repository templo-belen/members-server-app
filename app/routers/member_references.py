from typing import Optional

from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.member_references import MembersReferenceInformation
from app.services.auth import AuthService
from app.services.member_references import MembersReferenceService


class MembersReferencesRouter:
    def __init__(self):
        self.router = APIRouter(prefix="/members-references", tags=["members-references"])
        self.auth_service = AuthService()
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get(
            "/{member_id}",
            response_model=Optional[MembersReferenceInformation],
            #dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def find_by_id(member_id, db: Session = Depends(get_db)):
            member_reference_service = MembersReferenceService(db)
            member_references = member_reference_service.find_by_id(member_id)
            if not member_references:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member_references
