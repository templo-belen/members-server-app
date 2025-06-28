from pydantic import BaseModel, ConfigDict


class FeatureResponse(BaseModel):
    code: str
    name: str

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
