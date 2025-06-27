from tests.utils import get_auth_headers

reference_update = {
    "id": 1,
    "totalTime": 24,
    "churchName": "Templo de la Fe",
    "mainPastorName": "Pastor Pedro Rosas",
    "leavingReason": "Me fui de la ciudad",
}

def test_find_references_by_member_id__with_not_found_member__returns_404(client):
    response = client.get("/members/9999/references", headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 404


def test_find_references_by_member_id__with_existing_member__returns_200(client):
    response = client.get("/members/1/references", headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 200
    json_data = response.json()
    assert "references" in json_data or "reasons_for_congregating" in json_data


def test_update_member_reference__with_member_not_found__returns_404(client):
    response = client.put(
        "/members/9999/references",
        json=reference_update,
        headers=get_auth_headers(client, "admin", "12345"),
    )
    assert response.status_code == 404


def test_update_member_reference__with_reference_not_found__returns_404(client):
    response = client.put(
        "/members/1/references",
        json={**reference_update, "id": 9999},
        headers=get_auth_headers(client, "admin", "12345"),
    )
    assert response.status_code == 404


def test_update_member_reference__with_member_and_reference_ok__returns_200(client):
    response = client.put(
        "/members/3/references",
        json=reference_update,
        headers=get_auth_headers(client, "admin", "12345"),
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["churchName"] == "Templo de la Fe"
    assert data["mainPastorName"] == "Pastor Pedro Rosas"
    assert data["leavingReason"] == "Me fui de la ciudad"
