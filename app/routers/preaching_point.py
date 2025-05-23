from typing import Optional, List

from fastapi import Depends, APIRouter

from app.database import get_db, Session
from app.models import PreachingPointInformation
from app.services import AuthService, PreachingPointService


class PreachingPointRouter:
    def __init__(self, preaching_point_service: PreachingPointService):
        self.router = APIRouter(prefix="/preaching-points", tags=["preaching-points"])
        self.auth_service = AuthService()
        self._setup_routes()
        self.preaching_point_service = preaching_point_service

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get(
            "/",
            response_model=Optional[List[PreachingPointInformation]] | None,
            # dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def get_all(db: Session = Depends(get_db)):
            return self.preaching_point_service.get_all(db)
