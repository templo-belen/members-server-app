from typing import List, Optional

from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.member import MemberBasicInformation, MemberPersonalInformation
from app.models.member_dew import MembersDEWInformation
from app.models.member_general_data import MembersGeneralDataInformation
from app.models.member_references import MembersReferenceInformation
from app.services.auth import AuthService
from app.services.member import MemberService
from app.services.member_dew import MembersDEWService
from app.services.member_general_data import MembersGeneralDataService
from app.services.member_references import MembersReferenceService


class MemberRouter:
    def __init__(self):
        self.router = APIRouter(prefix="/members", tags=["members"])
        self.auth_service = AuthService()
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get(
            "/",
            response_model=Optional[List[MemberBasicInformation]] | None,
            #dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def get_all(db: Session = Depends(get_db)):
            member_service = MemberService(db)
            return member_service.get_all()

        @self.router.get(
            "/{member_id}",
            response_model=MemberPersonalInformation,
            #dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def find_by_id(member_id, db: Session = Depends(get_db)):
            member_service = MemberService(db)
            member = member_service.find_by_id(member_id)
            if not member:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member

        @self.router.get(
            "/{member_id}/general-data",
            description="Get 'Member General Data' given the member ID",
            response_model=MembersGeneralDataInformation,
            #dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def find_general_data_by_member_id(member_id, db: Session = Depends(get_db)):
            member_general_data_service = MembersGeneralDataService(db)
            member_general_data = member_general_data_service.find_by_id(member_id)
            if not member_general_data:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member_general_data

        @self.router.get(
            "/{member_id}/references",
            response_model=Optional[MembersReferenceInformation],
            #dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def find_by_id(member_id, db: Session = Depends(get_db)):
            member_reference_service = MembersReferenceService(db)
            member_references = member_reference_service.find_by_id(member_id)
            if not member_references:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member_references

        @self.router.get(
            "/{member_id}/dew",
            response_model=Optional[MembersDEWInformation],
            #dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def find_by_id(member_id, db: Session = Depends(get_db)):
            member_dew_service = MembersDEWService(db)
            member_dew = member_dew_service.find_by_id(member_id)
            if not member_dew:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member_dew
