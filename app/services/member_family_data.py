from typing import List

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
from app.services.pydantic_tools import apply_updates_from_pydantic


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
            familyData=(FamilyDataResponse.model_validate(db_member_family_data) if db_member_family_data else None),
            childrenDataList=[MemberChildrenDataResponse.model_validate(child) for child in db_member_children],
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

    def update_member_family_data(
        self, member_id: int, member_family_data: MemberFamilyDataResponse, db: Session
    ) -> MemberFamilyDataResponse:
        member_to_update = db.query(Member).filter(Member.id == member_id).first()
        if not member_to_update:
            raise NotFoundException(f"El miembro con id {member_id} no existe.")

        family_data_to_update = None
        if member_family_data.family_data:
            family_data_to_update = (
                db.query(MemberFamilyData)
                .filter(
                    MemberFamilyData.id == member_family_data.family_data.id, MemberFamilyData.member_id == member_id
                )
                .first()
            )

        db_current_children = db.query(MemberChildren).filter(MemberChildren.member_id == member_id).all()

        if not family_data_to_update and not db_current_children:
            raise NotFoundException(f"El miembro con id {member_id} no tiene datos familiares para ser actualizados.")

        if member_family_data.family_data:
            apply_updates_from_pydantic(family_data_to_update, member_family_data.family_data)

        updated_children = []
        if db_current_children or member_family_data.children_data_list:
            self.update_childrenList(member_id, db_current_children, member_family_data.children_data_list, db)
            db.flush()
            updated_children = db.query(MemberChildren).filter(MemberChildren.member_id == member_id).all()

        member_to_update.updated_by = current_user_ctx.get().username
        db.commit()
        db.refresh(member_to_update)
        if member_family_data.family_data:
            db.refresh(family_data_to_update)

        return MemberFamilyDataResponse(
            familyData=(FamilyDataResponse.model_validate(family_data_to_update) if family_data_to_update else None),
            childrenDataList=[MemberChildrenDataResponse.model_validate(child) for child in updated_children],
        )

    def update_childrenList(
        self,
        member_id: int,
        db_current_children,
        updated_children_list_data: List[MemberChildrenDataResponse],
        db: Session,
    ):
        current_children_dict = {}
        if db_current_children:
            current_children_dict = {child.id: child for child in db_current_children}
            children_update_ids = {child.id for child in updated_children_list_data if child.id != 0}

            # Deleting children
            for child in db_current_children:
                if child.id not in children_update_ids:
                    db.delete(child)

        # Updating or creating children
        for child in updated_children_list_data:
            if child.id == 0:
                db_new_child_data = MemberChildren(**child.model_dump(exclude_unset=True))
                db_new_child_data.id = None
                db_new_child_data.member_id = member_id
                db.add(db_new_child_data)
            else:
                db_update_child_data = current_children_dict.get(child.id)
                if db_update_child_data:
                    apply_updates_from_pydantic(db_update_child_data, child)
