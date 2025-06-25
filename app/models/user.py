from pydantic import BaseModel, ConfigDict, Field

from app.models.role import RoleResponse


class LoginRequest(BaseModel):
    id: int
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
    role: RoleResponse | None

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class CreateUpdateUserRequest(BaseModel):
    username: str = Field(min_length=5)
    full_name: str = Field(alias="fullName", min_length=5)
    password: str = Field(min_length=5)
    role_id: int = Field(alias="role", gt=0)

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class PasswordChangeRequest(BaseModel):
    current_password: str = Field(alias="currentPassword")
    new_password: str = Field(alias="newPassword")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
