from typing import List, Optional

from fastapi import Depends, APIRouter, HTTPException, status

from app.database import get_db, Session
from app.models import (
    MemberListItemResponse,
    MemberPersonalInformationResponse,
    MemberGeneralDataResponse,
    MemberReferenceResponse,
    MembersDEWResponse
)
from app.services import (
    AuthService,
    MemberService,
    MembersDEWService,
    MembersGeneralDataService,
    MembersReferenceService,
)


class MemberRouter:
    def __init__(self, member_service: MemberService,
                       member_general_data_service: MembersGeneralDataService,
                       member_reference_service: MembersReferenceService,
                       member_dew_service: MembersDEWService):
        self.router = APIRouter(prefix="/members", tags=["members"])
        self.auth_service = AuthService()
        self._setup_routes()
        self.member_service = member_service
        self.member_general_data_service = member_general_data_service
        self.member_reference_service = member_reference_service
        self.member_dew_service = member_dew_service

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get(
            "/",
            response_model=Optional[List[MemberListItemResponse]] | None,
            #dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def get_all(db: Session = Depends(get_db)):
            return self.member_service.get_all(db)

        @self.router.get(
            "/{member_id}",
            response_model=MemberPersonalInformationResponse,
            #dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def find_by_id(member_id, db: Session = Depends(get_db)):
            member = self.member_service.find_by_id(member_id, db)
            if not member:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member

        @self.router.get(
            "/{member_id}/general-data",
            description="Get 'Member General Data' given the member ID",
            response_model=MemberGeneralDataResponse,
            #dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def find_general_data_by_member_id(member_id, db: Session = Depends(get_db)):
            member_general_data = self.member_general_data_service.find_by_id(member_id, db)
            if not member_general_data:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member_general_data

        @self.router.get(
            "/{member_id}/references",
            response_model=Optional[MemberReferenceResponse],
            #dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def find_by_id(member_id, db: Session = Depends(get_db)):
            member_references = self.member_reference_service.find_by_id(member_id, db)
            if not member_references:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member_references

        @self.router.get(
            "/{member_id}/dew",
            response_model=Optional[MembersDEWResponse],
            #dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def find_by_id(member_id, db: Session = Depends(get_db)):
            member_dew = self.member_dew_service.find_by_id(member_id, db)
            if not member_dew:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member_dew
