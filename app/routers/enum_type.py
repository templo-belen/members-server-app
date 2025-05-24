from typing import Optional

from fastapi import APIRouter
from fastapi import Query

from app.services import AuthService, get_enums_by_names

class EnumTypeRouter:
    def __init__(self):
        self.router = APIRouter(prefix="/enums", tags=["enums"])
        self.auth_service = AuthService()
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get("/")
        # dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        def get_enums(names: Optional[list[str]] = Query(None, alias="names")):
            return get_enums_by_names(names)
