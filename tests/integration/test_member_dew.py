from tests.utils import get_auth_headers

dew_updating = {
    "ministrationDate": "2025-06-04",
    "worker1": "Jhon",
    "worker2": "Peter",
    "isSharingTestimony": True,
    "isPublishingTestimony": True,
    "isPublishingTestimonyName": False,
    "isAgreedShareTestimony": False,
    "id": 1,
}

dew_creation = {
    "ministrationDate": "2025-06-04",
    "worker1": "Jhon",
    "worker2": "Peter",
    "isSharingTestimony": True,
    "isPublishingTestimony": True,
    "isPublishingTestimonyName": False,
    "isAgreedShareTestimony": False,
}


def test_find_dew_by_member_id__with_not_found_member_id__returns_404(client):
    response = client.get("/members/100000/dew", headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 404


def test_find_dew_by_member_id__with_existing_member_id__returns_200(client):
    response = client.get("/members/1/dew", headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 200
    assert response.json()["memberId"] == 1


def test_create_dew__with_member_has_already_dew__returns_409(client):
    create_response = client.post(
        "/members/1/dew", json=dew_creation, headers=get_auth_headers(client, "admin", "12345")
    )
    assert create_response.status_code == 409


def test_create_dew__with_member_not_found__returns_404(client):
    create_response = client.post(
        "/members/10001/dew", json=dew_creation, headers=get_auth_headers(client, "admin", "12345")
    )
    assert create_response.status_code == 404


def test_create_dew__with_member_ok__returns_200(client):
    create_response = client.post(
        "/members/101/dew", json=dew_creation, headers=get_auth_headers(client, "admin", "12345")
    )
    assert create_response.status_code == 200
    assert create_response.json()["memberId"] == 101
    assert create_response.json()["id"] > 0
    assert create_response.json()["worker1"] == "Jhon"
    assert create_response.json()["worker2"] == "Peter"
    assert create_response.json()["isSharingTestimony"] is True
    assert create_response.json()["isPublishingTestimony"] is True
    assert create_response.json()["isAgreedShareTestimony"] is False


def test_update_dew__with_member_not_found__returns_404(client):
    create_response = client.put(
        "/members/1000/dew", json=dew_updating, headers=get_auth_headers(client, "admin", "12345")
    )
    assert create_response.status_code == 404


def test_update_dew__with_member_has_not_dew__returns_404(client):
    create_response = client.put(
        "/members/101/dew", json=dew_updating, headers=get_auth_headers(client, "admin", "12345")
    )
    assert create_response.status_code == 404


def test_update_dew__with_member_ok__returns_200(client):
    create_response = client.put(
        "/members/1/dew", json=dew_updating, headers=get_auth_headers(client, "admin", "12345")
    )
    assert create_response.status_code == 200
    assert create_response.json()["memberId"] == 1
    assert create_response.json()["id"] == 1
    assert create_response.json()["worker1"] == "Jhon"
    assert create_response.json()["worker2"] == "Peter"
    assert create_response.json()["isSharingTestimony"]
    assert create_response.json()["isPublishingTestimony"]
    assert not create_response.json()["isAgreedShareTestimony"]
