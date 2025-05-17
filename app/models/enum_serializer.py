from typing import Annotated, TypeVar
from pydantic import BeforeValidator, PlainSerializer

T = TypeVar("T")
def SerializedEnumByName(E: type[T]) -> type[T]:
    return Annotated[
        E,
        BeforeValidator(lambda v: v if isinstance(v, E) else E(v)),
        PlainSerializer(lambda v: v.name if isinstance(v, E) else v, return_type=str, when_used="always")
    ]
