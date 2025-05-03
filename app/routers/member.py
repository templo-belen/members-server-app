from typing import List, Optional

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.member import MemberBasicInformation
from app.services.auth import AuthService
from app.services.member import MemberService


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
            # Esto funciona, por ahora estaremos sin seguridad para agilizar
            # Descomentar para agregar autorización
            #dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def get_all(db: Session = Depends(get_db)):
            member_service = MemberService(db)
            return member_service.get_all()
