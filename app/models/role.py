from pydantic import BaseModel, ConfigDict


class RoleResponse(BaseModel):
    id: int
    code: str
    name: str

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
