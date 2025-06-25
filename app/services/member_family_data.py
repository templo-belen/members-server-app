from sqlalchemy.orm import Session

from app.database import Member, MemberFamilyData
from app.database.member_children import MemberChildren
from app.middlewares import current_user_ctx
from app.models import (
    CreateFamilyDataRequest,
    CreateMemberChildrenDataRequest,
    CreateMemberFamilyDataRequest,
    FamilyDataResponse,
    MemberChildrenDataResponse,
    MemberFamilyDataResponse,
)
from app.services import ConflictException, NotFoundException


class MembersFamilyDataService:
    def __init__(self):
        pass

    def find_by_member_id(self, member_id, db: Session) -> MemberFamilyDataResponse | None:
        member_family_data = db.query(MemberFamilyData).filter(MemberFamilyData.member_id == member_id).first()
        member_family_data_response = None
        if member_family_data:
            member_family_data_response = FamilyDataResponse.model_validate(member_family_data)

        member_children_list = db.query(MemberChildren).filter(MemberChildren.member_id == member_id).all()
        member_children_response = []
        if member_children_list:
            member_children_response = [
                MemberChildrenDataResponse.model_validate(child) for child in member_children_list
            ]

        if not member_family_data_response and not member_children_response:
            return None

        return MemberFamilyDataResponse(
            familyData=member_family_data_response, childrenDataList=member_children_response
        )

    def create_member_family_data(
        self, member_id: int, new_member_family_data: CreateMemberFamilyDataRequest, db: Session
    ) -> MemberFamilyDataResponse:
        member = db.query(Member).filter(Member.id == member_id).first()
        if not member:
            raise NotFoundException(f"El miembro con id {member_id} no existe.")

        self.validate_member_family_data(member_id, db)

        db_member_family_data = None
        if new_member_family_data.family_data:
            db_member_family_data = self.add_family_data(member_id, new_member_family_data.family_data, db)

        db_member_children = []
        if new_member_family_data.children_data_list and len(new_member_family_data.children_data_list) > 0:
            db_member_children = self.add_children_data(member_id, new_member_family_data.children_data_list, db)

        member.updated_by = current_user_ctx.get().username
        db.commit()
        db.refresh(member)

        return MemberFamilyDataResponse(
            family_data=(FamilyDataResponse.model_validate(db_member_family_data) if db_member_family_data else None),
            children_data_list=[MemberChildrenDataResponse.model_validate(child) for child in db_member_children],
        )

    def validate_member_family_data(self, member_id: int, db: Session):
        member_family_data = self.find_by_member_id(member_id, db)
        if member_family_data:
            raise ConflictException(f"El miembro con id {member_id} ya tiene datos familiares")

    def add_family_data(self, member_id: int, family_data: CreateFamilyDataRequest, db: Session):
        db_member_family_data = MemberFamilyData(**family_data.model_dump(exclude_unset=True))
        db_member_family_data.member_id = member_id
        db.add(db_member_family_data)
        db.flush()
        return db_member_family_data

    def add_children_data(self, member_id: int, children_data_list: [CreateMemberChildrenDataRequest], db: Session):
        db_member_children = []
        for child in children_data_list:
            db_child_data = MemberChildren(**child.model_dump(exclude_unset=True))
            db_child_data.member_id = member_id
            db_member_children.append(db_child_data)

        db.add_all(db_member_children)
        db.flush()
        return db_member_children
