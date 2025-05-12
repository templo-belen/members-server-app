from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.enum_type import EnumTypeRouter
from app.routers.health import HealthRouter
from app.routers.login import LoginRouter
from app.routers.member import MemberRouter
from app.routers.preaching_point import PreachingPointRouter
from app.routers.user import UserRouter
from app.services.health import HealthService

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
app.include_router(LoginRouter().get_router())

# Users
app.include_router(UserRouter().get_router())

# Members
app.include_router(MemberRouter().get_router())

# Preaching points
app.include_router(PreachingPointRouter().get_router())

# Enum types
app.include_router(EnumTypeRouter().get_router())
