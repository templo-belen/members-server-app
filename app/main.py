from fastapi import FastAPI

from app.routers.health import HealthRouter
from app.routers.login import LoginRouter
from app.routers.user import UserRouter
from app.services.health import HealthService

app = FastAPI()

health_service = HealthService()
health_router = HealthRouter(health_service)
app.include_router(health_router.get_router())

# Login
login_router = LoginRouter()
app.include_router(login_router.get_router())

# Users
user_router = UserRouter()
app.include_router(user_router.get_router())
