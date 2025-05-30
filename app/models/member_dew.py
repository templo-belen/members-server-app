from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class MembersDEWResponse(BaseModel):
    member_id: int = Field(description="Member ID", alias="memberId")

    ministration_date: Optional[datetime] = Field(description="Ministration date", alias="ministrationDate")
    worker_1: Optional[str] = Field(description="Worker 1", alias="worker1")
    worker_2: Optional[str] = Field(description="Worker 2", alias="worker2")
    is_sharing_testimony: Optional[bool] = Field(description="Is sharing testimony", alias="isSharingTestimony")
    is_publishing_testimony: Optional[bool] = Field(description="Is publishing testimony", alias="isPublishingTestimony")
    is_publishing_testimony_name: Optional[bool] = Field(description="Is publishing testimony name", alias="isPublishingTestimonyName")
    is_agreed_share_testimony: Optional[bool] = Field(description="Is agreed share", alias="isAgreedShareTestimony")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )
