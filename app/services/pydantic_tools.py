from pydantic import BaseModel


def apply_updates_from_pydantic(instance, pydantic_model : BaseModel, exclude_unset=True):
    """
    Updates the attributes of a SQLAlchemy database model
    :param instance: SQLAlchemy model
    :param pydantic_model: pydantic model
    :param exclude_unset: Boolean
    """
    update_data = pydantic_model.model_dump(exclude_unset=exclude_unset)
    for key, value in update_data.items():
        setattr(instance, key, value)
