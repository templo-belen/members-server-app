from pydantic import BaseModel, Field


class HealthReponse(BaseModel):
    application_health: str = Field(description="Estado actual de la aplicacion")
    database_health: str = Field(description="Estado actual de la bd")
