from typing import Annotated, TypeVar, Callable

from fastapi import HTTPException, Query
from pydantic import BeforeValidator, PlainSerializer

T = TypeVar("T")

def serialized_enum_by_name(e: type[T]) -> type[T]:
    """
        This generic function receives an Enum type and transforms the name into the appropriate enum value.

        - `BeforeValidator(...)`: It is executed before validation.
        If `v` is already an `Enum`, it remains it as is. If `v` is an `Enum`'s name (e.g., o_positive), it returns the Enum (e.g., BloodType.o_positive`).

        - PlainSerializer(..., return_type=str, when_used="always"): This is executed when converting to JSON.
        If the value is an `Enum` (e.g., `BloodType.o_positive`), it returns its name: `"o_positive"`.
        If for some reason it's already a string, it returns it as is (this prevents errors).
    """

    def enum_from_name(v) -> type[T]:
        if isinstance(v, e):
            return v
        if v in e.__members__:
            return e.__members__[v]
        raise ValueError(f"value {v} not allowed as {e}")

    return Annotated[
        e,
        BeforeValidator(enum_from_name),
        PlainSerializer(lambda v: v.name if isinstance(v, e) else v, return_type=str, when_used="always")
    ]


def parse_enum_by_name(enum_class: type[T], alias: str = None, description: str = None) -> Callable[[str], T]:
    def parser(value: str = Query(..., alias=alias, description=description)) -> T:
        try:
            return enum_class[value]
        except KeyError:
            raise HTTPException(
                status_code=422,
                detail=f"'{value}' is not valid. Use one of: {[e.name for e in enum_class]}"
            )
    return parser
