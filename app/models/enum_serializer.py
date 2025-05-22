from typing import Annotated, TypeVar, Callable

from fastapi import HTTPException, Query
from pydantic import BeforeValidator, PlainSerializer

T = TypeVar("T")

def serialized_enum_by_name(e: type[T]) -> type[T]:
    """
        This generic function receives an Enum and transforms the values or names of the enums.

        - BeforeValidator(lambda v: v if isinstance(v, E) else E(v)): It is executed before validation.
        If v is already an Enum,it leaves it as is. If v is an Enum value (e.g., 0+), it attempts to convert it to an Enum (e.g., BloodType.o_positive).

        - PlainSerializer(lambda v: v.name if isinstance(v, E) else v, return_type=str, when_used="always"): This is executed when converting to JSON.
        If the value is an Enum (e.g., BloodType.o_positive), it returns its name: "o_positive".
        If for some reason it's already a string, it returns it as is (this prevents errors).
    """

    return Annotated[
        e,
        BeforeValidator(lambda v: v if isinstance(v, e) else e(v)),
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
