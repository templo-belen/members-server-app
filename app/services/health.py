from app.models.health import HealthReponse


class HealthService:
    def __init__(
        self
        # TODO: pasar la bd como parametro en el init para obtener su estado
    ):
        pass

    def get_application_health(
        self
    ) -> HealthReponse:
        # TODO: obtener el estado actual de la bd
        return HealthReponse(
            application_health="OK",
            database_health="OK"
        )
