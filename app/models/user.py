from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)

from app.models.role import RoleInformation


class LoginRequest(BaseModel):
    id : int
    username: str
    password: str

class LoginResponse(BaseModel):
    username: str
    full_name: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id: int
    username: str
    full_name: str
    role: RoleInformation | None
    
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )

class CreateUserRequest(BaseModel):
    username: str
    full_name: str = Field(alias="fullName")
    password: str
    role_id: int = Field(alias="role")
    
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )
