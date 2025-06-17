from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.database import get_db
from app.models import MemberADNResponse
from app.services import AuthService, MemberADNService


class MemberADNRouter:
    def __init__(self, member_adn_service: MemberADNService, auth_service: AuthService):
        self.member_adn_service = member_adn_service
        self.auth_service = auth_service

        self.router = APIRouter(prefix="/members/{member_id}/adn", tags=["member-adn"])
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get(
            "/",
            response_model=Optional[MemberADNResponse],
            # dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def find_adn_by_id(member_id: int, db: Session = Depends(get_db)):
            member_adn = self.member_adn_service.find_by_member_id(member_id, db)
            if not member_adn:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member_adn
