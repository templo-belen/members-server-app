import copy

from tests.utils import get_auth_headers

member_creation_json_1 = {
    "familyData": {
        "maritalStatus": "soltero",
        "fathersName": "Henry Gómez",
        "mothersName": None,
        "spouseName": None,
        "spouseOccupation": None,
        "marriageRegistrationNumber": None,
        "housingType": "propia",
    },
    "childrenDataList": None,
}

member_creation_json_2 = {
    "familyData": {
        "maritalStatus": "soltero",
        "fathersName": "Henry Gómez",
        "mothersName": "María Pérez",
        "spouseName": None,
        "spouseOccupation": None,
        "marriageRegistrationNumber": None,
        "housingType": "propia",
    },
    "childrenDataList": [
        {"childName": "Christian", "childOccupation": "Estudiante"},
        {"childName": "María", "childOccupation": "Estudiante"},
    ],
}

member_creation_json_3 = {
    "familyData": None,
    "childrenDataList": [
        {"childName": "Christian", "childOccupation": "Estudiante"},
        {"childName": "María", "childOccupation": "Estudiante"},
    ],
}

member_updating_json_1 = {
    "familyData": {
        "id": 1,
        "memberId": 3,
        "maritalStatus": "viudo",
        "fathersName": "Carlos Ramírez",
        "mothersName": "Lucía Herrera",
        "spouseName": None,
        "spouseOccupation": None,
        "marriageRegistrationNumber": None,
        "housingType": "alquiler",
    },
    "childrenDataList": [
        {"id": 1, "memberId": 3, "childName": "Lucía Ramírez", "childOccupation": "Estudiante"},
        {"id": 2, "memberId": 3, "childName": "Mateo Ramírez", "childOccupation": "Programador Junior"},
        {"id": 0, "memberId": 3, "childName": "Recien nacido", "childOccupation": "Es un bebé"},
    ],
}

member_updating_json_2 = {
    "familyData": {
        "id": 2,
        "memberId": 4,
        "maritalStatus": "casado",
        "fathersName": "Roberto Díaz",
        "mothersName": "Sandra Molina",
        "spouseName": None,
        "spouseOccupation": None,
        "marriageRegistrationNumber": None,
        "housingType": "alquiler",
    },
    "childrenDataList": [{"id": 0, "memberId": 3, "childName": "Recien nacido", "childOccupation": "Es un bebé"}],
}

member_updating_json_3 = {
    "familyData": None,
    "childrenDataList": [{"id": 3, "memberId": 7, "childName": "Sofía Herrera", "childOccupation": "Arquitecta"}],
}


def test_find_family_data_by_member_id__with_not_found_member_id__returns_404(client):
    response = client.get("/members/100000/family-data", headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 404


def test_find_family_data_by_member_id__with_existing_member_id__returns_200(client):
    response = client.get("/members/3/family-data", headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 200
    assert response.json()["familyData"]["memberId"] == 3


def test_create_family_data__with_member_has_already_family_data__returns_409(client):
    create_response = client.post(
        "/members/3/family-data", json=member_creation_json_1, headers=get_auth_headers(client, "admin", "12345")
    )
    assert create_response.status_code == 409


def test_create_family_data__with_member_not_found__returns_404(client):
    create_response = client.post(
        "/members/1000/family-data", json=member_creation_json_1, headers=get_auth_headers(client, "admin", "12345")
    )
    assert create_response.status_code == 404


def test_create_family_data__with_member_ok__returns_200(client):
    headers = get_auth_headers(client, "admin", "12345")

    # With family_data but not children
    create_response = client.post("/members/101/family-data", json=member_creation_json_1, headers=headers)
    assert create_response.status_code == 200
    assert create_response.json()["familyData"]["memberId"] == 101
    assert create_response.json()["familyData"]["id"] > 0
    assert not create_response.json()["childrenDataList"]

    # With family data and children
    create_response = client.post("/members/102/family-data", json=member_creation_json_2, headers=headers)
    assert create_response.status_code == 200
    assert create_response.json()["familyData"]["memberId"] == 102
    assert create_response.json()["familyData"]["id"] > 0
    assert create_response.json()["childrenDataList"] and len(create_response.json()["childrenDataList"]) == 2
    assert create_response.json()["childrenDataList"][0]["id"] > 0
    assert create_response.json()["childrenDataList"][0]["memberId"] == 102

    # With children data but not family data
    create_response = client.post("/members/103/family-data", json=member_creation_json_3, headers=headers)
    assert create_response.status_code == 200
    assert not create_response.json()["familyData"]
    assert create_response.json()["childrenDataList"] and len(create_response.json()["childrenDataList"]) == 2
    assert create_response.json()["childrenDataList"][0]["id"] > 0
    assert create_response.json()["childrenDataList"][0]["memberId"] == 103


def test_update_family_data__with_member_not_found__returns_404(client):
    create_response = client.put(
        "/members/1000/family-data", json=member_updating_json_1, headers=get_auth_headers(client, "admin", "12345")
    )
    assert create_response.status_code == 404


def test_update_family_data__with_member_without_family_data__returns_404(client):
    without_family_data_json = copy.deepcopy(member_updating_json_1)
    without_family_data_json["familyData"]["id"] = 101
    create_response = client.put(
        "/members/101/family-data", json=without_family_data_json, headers=get_auth_headers(client, "admin", "12345")
    )
    assert create_response.status_code == 404


def test_update_family_data__with_member_ok__returns_200(client):
    headers = get_auth_headers(client, "admin", "12345")
    update_response = client.put("/members/3/family-data", json=member_updating_json_1, headers=headers)

    # Adding a new child and updating family data
    assert update_response.status_code == 200
    assert update_response.json()["familyData"]["memberId"] == 3
    assert update_response.json()["familyData"]["id"] == 1
    assert update_response.json()["familyData"]["maritalStatus"] == "viudo"
    assert not update_response.json()["familyData"]["spouseName"]
    assert update_response.json()["familyData"]["housingType"] == "alquiler"
    assert len(update_response.json()["childrenDataList"]) == 3

    # Adding a new child
    update_response = client.put("/members/4/family-data", json=member_updating_json_2, headers=headers)
    assert update_response.status_code == 200
    assert update_response.json()["familyData"]["memberId"] == 4
    assert update_response.json()["familyData"]["id"] == 2
    assert update_response.json()["familyData"]["maritalStatus"] == "casado"
    assert update_response.json()["familyData"]["fathersName"] == "Roberto Díaz"
    assert update_response.json()["familyData"]["housingType"] == "alquiler"
    assert len(update_response.json()["childrenDataList"]) == 1

    # Deleting a child
    update_response = client.put("/members/7/family-data", json=member_updating_json_3, headers=headers)
    assert update_response.status_code == 200
    assert not update_response.json()["familyData"]
    assert len(update_response.json()["childrenDataList"]) == 1
