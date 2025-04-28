from fastapi import APIRouter, Response

from app.services.health import HealthService


class HealthRouter:
    def __init__(self, service: HealthService):
        self.service = service

    def get_router(self):
        router = APIRouter(
            tags=["health"],
        )

        @router.get("/health")
        async def health_check(response: Response):
            # TODO: Add postgres DB health check
            response.status_code = 200
            return self.service.get_application_health()

        return router
