from typing import Dict, List

from fastapi import HTTPException

from app.models import (
    BloodType,
    CellLeadershipType,
    GenderType,
    HousingType,
    LeadershipType,
    LeavingReasonType,
    MaritalStatusType,
    NameValueResponse,
    RoleType,
)

enum_map = {
    "marital-status": MaritalStatusType,
    "gender": GenderType,
    "role": RoleType,
    "cell-leadership": CellLeadershipType,
    "leadership": LeadershipType,
    "housing": HousingType,
    "leaving-reason": LeavingReasonType,
    "blood-type": BloodType,
}

def get_enums_by_names(names: list[str]) -> Dict[str, List[NameValueResponse]]:
    """
    Returns all the enums by the given names.
    :param names: enums names
    :return: dictionary of enums
    """
    response = {}
    if not names:
        selected_enum_map = enum_map    # Return all the enums
    else:
        selected_enum_map = {}
        for name in names:
            enum_class = enum_map.get(name)
            if not enum_class:
                raise HTTPException(status_code=400, detail=f"Enum '{name}' not found")
            selected_enum_map[name] = enum_class

    for name, enum_class in selected_enum_map.items():
        response[name] = [NameValueResponse(name=e.name, value=e.value) for e in enum_class]

    return response
