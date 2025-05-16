from pydantic import BaseModel

from app.models.role import RoleInformation


class LoginRequest(BaseModel):
    id : int
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    username: str
    full_name: str
    role: RoleInformation | None
