from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import (
    MemberGeneralDataResponse, CreateMemberGeneralDataRequest,
)
from app.services import (
    AuthService,
    MembersGeneralDataService,
)


class MemberGeneralDataRouter:
    def __init__(self,
                 member_general_data_service: MembersGeneralDataService,
                 auth_service: AuthService,
                 ):
        self.member_general_data_service = member_general_data_service
        self.auth_service = auth_service
        self.router = APIRouter(prefix="/members/{member_id}/general-data", tags=["member-general-data"])
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get(
            "/",
            description="Get 'Member General Data' given the member ID",
            response_model=MemberGeneralDataResponse,
            # dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def find_general_data_by_member_id(member_id : int, db: Session = Depends(get_db)):
            member_general_data = self.member_general_data_service.find_by_member_id(member_id, db)
            if not member_general_data:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member_general_data

        @self.router.post(
            "/",
            description="Save 'Member General Data' given the member ID",
            response_model=MemberGeneralDataResponse,
            dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def find_general_data_by_member_id(new_member_data : CreateMemberGeneralDataRequest, db: Session = Depends(get_db)):
            return self.member_general_data_service.create_member_general_data(new_member_data, db)
