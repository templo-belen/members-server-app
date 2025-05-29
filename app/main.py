from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    EnumTypeRouter,
    HealthRouter,
    LoginRouter,
    MemberRouter,
    PreachingPointRouter,
    UserRouter,
)
from app.services import (
    AuthService,
    HealthService,
    MemberService,
    MembersDEWService,
    MembersGeneralDataService,
    MembersReferenceService,
    PreachingPointService,
    UserService, MemberADNService,
)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Your Angular app's URL (adjust as needed)
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
preaching_point_service = PreachingPointService()
member_adn_service = MemberADNService()
app.include_router(MemberRouter(member_service, member_general_data_service, member_reference_service,
                                member_dew_service, preaching_point_service, member_adn_service)
                   .get_router())

# Preaching points
app.include_router(PreachingPointRouter(preaching_point_service).get_router())

# Enum types
app.include_router(EnumTypeRouter().get_router())
