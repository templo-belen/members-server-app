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
    MembersDEWResponse, )
from app.services import (
    AuthService,
    MembersDEWService,
)


class MemberDEWRouter:
    def __init__(self,
                 member_dew_service: MembersDEWService,
                 auth_service: AuthService):
        self.member_dew_service = member_dew_service
        self.auth_service = auth_service

        self.router = APIRouter(prefix="/members/{member_id}/dew", tags=["member-dew"])
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):

        @self.router.get(
            "/",
            response_model=Optional[MembersDEWResponse],
            # dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def find_dew_by_id(member_id : int, db: Session = Depends(get_db)):
            member_dew = self.member_dew_service.find_by_member_id(member_id, db)
            if not member_dew:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member_dew
