from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.member_general_data import MembersGeneralDataInformation
from app.services.auth import AuthService
from app.services.member_general_data import MembersGeneralDataService


class MembersGeneralDataRouter:
    def __init__(self):
        self.router = APIRouter(prefix="/members-general-data", tags=["members-general-data"])
        self.auth_service = AuthService()
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get(
            "/{member_id}",
            description="Get 'Member General Data' given the member_general_data ID",
            response_model=MembersGeneralDataInformation,
            #dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def find_by_id(member_id, db: Session = Depends(get_db)):
            member_general_data_service = MembersGeneralDataService(db)
            member_general_data = member_general_data_service.find_by_id(member_id)
            if not member_general_data:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member_general_data
