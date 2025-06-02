from typing import List, Optional

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import (
    CreateMemberRequest,
    MemberListItemResponse,
    MemberPersonalInformationResponse,
    CellLeadershipType,
    parse_enum_by_name,
    MemberBasicData,
    MemberFormValuesResponse,
    UpdateMemberRequest,
)
from app.services import (
    AuthService,
    MemberService,
    get_enums_by_names,
    PreachingPointService, )


class MemberRouter:
    def __init__(self,
                 member_service: MemberService,
                 preaching_point_service: PreachingPointService,
                 auth_service: AuthService):
        self.member_service = member_service
        self.preaching_point_service = preaching_point_service
        self.auth_service = auth_service

        self.router = APIRouter(prefix="/members", tags=["members"])
        self._setup_routes()

    def get_router(self):
        return self.router

    def _setup_routes(self):
        @self.router.get(
            "/",
            response_model=Optional[List[MemberListItemResponse]] | None,
            # dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def get_all(db: Session = Depends(get_db)):
            return self.member_service.get_all(db)

        @self.router.post(
            "/",
            response_model=MemberPersonalInformationResponse | None,
            dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def create_member(new_member: CreateMemberRequest, db: Session = Depends(get_db)):
            return self.member_service.create_member(new_member, db)

        @self.router.put(
            "/",
            response_model=MemberPersonalInformationResponse | None,
            dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def update_member(member_to_update: UpdateMemberRequest, db: Session = Depends(get_db)):
            return self.member_service.update_member(member_to_update, db)

        @self.router.get(
            "/init-form",
            response_model=MemberFormValuesResponse,
            # dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def get_init_data(db: Session = Depends(get_db)):
            enums = get_enums_by_names([
                "marital-status", "gender", "role", "cell-leadership",
                "leadership", "housing", "leaving-reason", "blood-type"
            ])
            zone_pastors = self.member_service.get_all_by_cell_leadership(CellLeadershipType.pastor_zona, db)
            preaching_points = self.preaching_point_service.get_all(db)

            return MemberFormValuesResponse(
                enums=enums,
                zone_pastors=zone_pastors,
                preaching_points=preaching_points
            )

        @self.router.get(
            "/by-cell-leadership",
            response_model=Optional[List[MemberBasicData]] | None,
            # dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def get_all_by_cell_leadership(
                cell_leadership: CellLeadershipType = Depends(
                    parse_enum_by_name(CellLeadershipType, alias="value",
                                       description="Enum name like 'pastor_zona'"
                                       )),
                db: Session = Depends(get_db)):
            return self.member_service.get_all_by_cell_leadership(cell_leadership, db)

        @self.router.get(
            "/{member_id}",
            response_model=MemberPersonalInformationResponse,
            # dependencies=[Depends(self.auth_service.require_role(["admin", "pastor"]))]
        )
        def find_by_id(member_id: int, db: Session = Depends(get_db)):
            member = self.member_service.find_by_id(member_id, db)
            if not member:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return member
