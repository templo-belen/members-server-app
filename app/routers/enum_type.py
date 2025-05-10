from fastapi import APIRouter, HTTPException
from fastapi import Query

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
        @self.router.get("/",  #
            #dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def get_enums(names: list[str] = Query(..., alias="names")):
            response = {}
            for name in names:
                enum_class = enum_map.get(name)
                if not enum_class:
                    raise HTTPException(status_code=404, detail=f"Enum '{name}' not found")
                response[name] = [{"name": e.name, "value": e.value} for e in enum_class]
            return response

