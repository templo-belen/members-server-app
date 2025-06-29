from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import RoleResponse
from app.services import AuthService, RoleService


class RoleRouter:
    def __init__(self, role_service: RoleService, auth_service: AuthService):
        self.auth_service = auth_service
        self.role_service = role_service

        self.router = APIRouter(prefix="/roles", tags=["roles"])
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get(
            "/",
            response_model=Optional[List[RoleResponse]] | None,
            dependencies=[Depends(self.auth_service.require_role(["admin"]))],
        )
        def get_all(db: Session = Depends(get_db)):
            return self.role_service.get_all(db)
