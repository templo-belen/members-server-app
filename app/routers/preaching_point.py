from typing import Optional, List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import PreachingPointInformation
from app.services import AuthService, PreachingPointService


class PreachingPointRouter:
    def __init__(self, preaching_point_service: PreachingPointService, auth_service: AuthService):
        self.auth_service = auth_service
        self.preaching_point_service = preaching_point_service
        
        self.router = APIRouter(prefix="/preaching-points", tags=["preaching-points"])
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get(
            "/",
            response_model=Optional[List[PreachingPointInformation]] | None,
            dependencies=[Depends(self.auth_service.require_role(["admin", "pastor", "readonly"]))]
        )
        def get_all(db: Session = Depends(get_db)):
            return self.preaching_point_service.get_all(db)
