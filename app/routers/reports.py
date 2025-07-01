from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.reports import ReportColumn
from app.services import AuthService, ReportsService


class ReportsRouter:
    def __init__(self, reports_service: ReportsService, auth_service: AuthService):
        self.reports_service = reports_service
        self.auth_service = auth_service

        self.router = APIRouter(prefix="/reports", tags=["reports"])
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):

        @self.router.get(
            "/columns",
            response_model=Optional[List[ReportColumn]],
            dependencies=[Depends(self.auth_service.require_role(["admin"]))],
        )
        def get_columns(db: Session = Depends(get_db)):
            available_columns = self.reports_service.get_columns(db)
            if not available_columns:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return available_columns
