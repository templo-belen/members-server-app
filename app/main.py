from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.enum_type import EnumTypeRouter
from app.routers.health import HealthRouter
from app.routers.login import LoginRouter
from app.routers.member import MemberRouter
from app.routers.preaching_point import PreachingPointRouter
from app.routers.user import UserRouter
from app.services.auth import AuthService
from app.services.health import HealthService
from app.services.member import MemberService
from app.services.member_dew import MembersDEWService
from app.services.member_general_data import MembersGeneralDataService
from app.services.member_references import MembersReferenceService
from app.services.preaching_point import PreachingPointService
from app.services.user import UserService

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Your Angular app's URL (adjust as needed)
    allow_credentials=True,
    allow_methods=["*"],  # Or specify: ["GET", "POST", "PUT", "DELETE", etc.]
    allow_headers=["*"],  # Or specify required headers
)

health_service = HealthService()
health_router = HealthRouter(health_service)
app.include_router(health_router.get_router())

# Login
user_service = UserService()
app.include_router(LoginRouter(user_service, AuthService()).get_router())

# Users
app.include_router(UserRouter(user_service).get_router())

# Members
member_service = MemberService()
member_general_data_service = MembersGeneralDataService()
member_reference_service = MembersReferenceService()
member_dew_service = MembersDEWService()
app.include_router(MemberRouter(member_service, member_general_data_service, member_reference_service,
                                member_dew_service)
                   .get_router())

# Preaching points
app.include_router(PreachingPointRouter(PreachingPointService()).get_router())

# Enum types
app.include_router(EnumTypeRouter().get_router())
