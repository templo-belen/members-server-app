from typing import Optional

from fastapi import APIRouter, HTTPException
from fastapi import Query

from app.models import (
    MaritalStatusType,
    GenderType,
    RoleType,
    CellLeadershipType,
    LeadershipType,
    HousingType,
    LeavingReasonType,
    BloodType
)
from app.services import AuthService


enum_map = {
    "marital-status": MaritalStatusType,
    "gender": GenderType,
    "role": RoleType,
    "cell-leadership": CellLeadershipType,
    "leadership": LeadershipType,
    "housing": HousingType,
    "leaving-reason": LeavingReasonType,
    "blood-type": BloodType,

}

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
            response = {}
            if not names:
                selected_enum_map = enum_map
            else:
                selected_enum_map = {}
                for name in names:
                    enum_class = enum_map.get(name)
                    if not enum_class:
                        raise HTTPException(status_code=404, detail=f"Enum '{name}' not found")
                    selected_enum_map[name] = enum_class

            for name, enum_class in selected_enum_map.items():
                response[name] = [{"name": e.name, "value": e.value} for e in enum_class]

            return response

