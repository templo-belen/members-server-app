from typing import Optional, List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.preaching_point import PreachingPointInformation
from app.services.auth import AuthService
from app.services.preaching_point import PreachingPointService


class PreachingPointRouter:
    def __init__(self):
        self.router = APIRouter(prefix="/preaching-points", tags=["preaching-points"])
        self.auth_service = AuthService()
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get(
            "/",
            response_model=Optional[List[PreachingPointInformation]] | None,
            # dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def get_all(db: Session = Depends(get_db)):
            preaching_point_service = PreachingPointService(db)
            return preaching_point_service.get_all()
