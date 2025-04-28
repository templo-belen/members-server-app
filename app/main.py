from fastapi import FastAPI

from app.routers.health import HealthRouter
from app.services.health import HealthService

app = FastAPI()

health_service = HealthService()

health_router = HealthRouter(health_service)

app.include_router(health_router.get_router())
