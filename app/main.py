from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.exception_handler import setup_exception_handles
from app.middlewares import UserAwareMiddleware
from app.routers import (
    EnumTypeRouter,
    HealthRouter,
    LoginRouter,
    MemberRouter,
    PreachingPointRouter,
    UserRouter,
    MemberGeneralDataRouter,
    MemberReferenceRouter, MemberDEWRouter, MemberFamilyDataRouter,
)
from app.services import (
    AuthService,
    HealthService,
    MemberService,
    MembersDEWService,
    MembersGeneralDataService,
    MembersReferenceService,
    PreachingPointService,
    UserService,
    MembersFamilyDataService,
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Your Angular app's URL (adjust as needed)
    allow_credentials=True,
    allow_methods=["*"],  # Or specify: ["GET", "POST", "PUT", "DELETE", etc.]
    allow_headers=["*"],  # Or specify required headers
)

# Used by all routers and auth middleware
user_service = UserService()
auth_service = AuthService(user_service)
app.add_middleware(
    UserAwareMiddleware,
    auth_service=auth_service,
)

health_service = HealthService()
health_router = HealthRouter(health_service)
app.include_router(health_router.get_router())

# Login
app.include_router(LoginRouter(user_service, auth_service).get_router())

# Users
app.include_router(UserRouter(user_service, auth_service).get_router())

# Members
member_service = MemberService()
preaching_point_service = PreachingPointService()
app.include_router(MemberRouter(member_service,
                                preaching_point_service,
                                auth_service)
                   .get_router())

app.include_router(MemberGeneralDataRouter(MembersGeneralDataService(), auth_service).get_router())
app.include_router(MemberReferenceRouter(MembersReferenceService(), auth_service).get_router())
app.include_router(MemberDEWRouter(MembersDEWService(), auth_service).get_router())
app.include_router(MemberFamilyDataRouter(MembersFamilyDataService(), auth_service).get_router())

# Preaching points
app.include_router(PreachingPointRouter(preaching_point_service, auth_service).get_router())

# Enum types
app.include_router(EnumTypeRouter(auth_service).get_router())

app = setup_exception_handles(app)
