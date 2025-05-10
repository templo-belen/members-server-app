from fastapi import APIRouter, HTTPException

from app.models.enum_type import MaritalStatusType, GenderType, RoleType, CellLeadershipType, LeadershipType, \
    HousingType, LeavingReasonType
from app.services.auth import AuthService
from fastapi import APIRouter, HTTPException

from app.models.enum_type import MaritalStatusType, GenderType, RoleType, CellLeadershipType, LeadershipType, \
    HousingType, LeavingReasonType
from app.services.auth import AuthService

enum_map = {
    "marital-status": MaritalStatusType,
    "gender": GenderType,
    "role": RoleType,
    "cell-leadership": CellLeadershipType,
    "leadership": LeadershipType,
    "housing": HousingType,
    "leaving-reason": LeavingReasonType,
}

class EnumTypeRouter:
    def __init__(self):
        self.router = APIRouter(prefix="/enums", tags=["enums"])
        self.auth_service = AuthService()
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get("/enums/{enum_name}",
            #dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def get_enum_values(enum_name: str):
            enum_class = enum_map.get(enum_name)
            if not enum_class:
                raise HTTPException(status_code=404, detail="Enum not found")
            return [{"name": e.name, "value": e.value} for e in enum_class]


