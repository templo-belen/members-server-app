from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import CreateMemberFamilyDataRequest, MemberFamilyDataResponse
from app.services import AuthService, MembersFamilyDataService


class MemberFamilyDataRouter:
    def __init__(self, member_family_data_service: MembersFamilyDataService, auth_service: AuthService):
        self.member_family_data_service = member_family_data_service
        self.auth_service = auth_service

        self.router = APIRouter(prefix="/members/{member_id}/family-data", tags=["member-family-data"])
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):

        @self.router.get(
            "/",
            response_model=Optional[MemberFamilyDataResponse],
            dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))],
        )
        def find_family_data_by_id(member_id: int, db: Session = Depends(get_db)):
            member_family_data = self.member_family_data_service.find_by_member_id(member_id, db)
            if not member_family_data:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member_family_data

        @self.router.post(
            "/",
            description="Save 'Member Family Data' given the member ID",
            response_model=MemberFamilyDataResponse,
            dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))],
        )
        def save_general_data_by_member_id(
            member_id: int, new_member_data: CreateMemberFamilyDataRequest, db: Session = Depends(get_db)
        ):
            return self.member_family_data_service.create_member_family_data(member_id, new_member_data, db)
