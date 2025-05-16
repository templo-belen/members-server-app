from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class MembersDEWResponse(BaseModel):
    id: int = Field(description="Member dew information DB id")
    member_id: int = Field(description="Member ID", alias="memberId")

    ministration_date: Optional[datetime] = Field(description="Ministration date")
    worker_1: Optional[str] = Field(description="Worker 1")
    worker_2: Optional[str] = Field(description="Worker 2")
    is_sharing_testimony: Optional[bool] = Field(description="Is sharing testimony")
    is_publishing_testimony: Optional[bool] = Field(description="Is publishing testimony")
    is_publishing_testimony_name: Optional[bool] = Field(description="Is publishing testimony name")
    is_agreed_share_testimony: Optional[bool] = Field(description="Is agreed share")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )
