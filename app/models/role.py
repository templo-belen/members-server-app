from pydantic import BaseModel


class RoleInformation(BaseModel):
    id: int
    code: str
    name: str
