from fastapi.testclient import TestClient

from tests.utils import get_auth_headers


def get_alter_user_request():
    return {"username": "username", "fullName": "John Doe", "password": "secret", "role": 1}


def test_update_user__with_valid_request__returns_200(client: TestClient):
    request = get_alter_user_request()
    request["username"] = "readonly"
    response = client.put("/users/3", json=request, headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 200


def test_update_user__with_invalid_request__returns_422(client: TestClient):
    request = get_alter_user_request()
    request["username"] = None
    response = client.put("/users/3", json=request, headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 422

    request = get_alter_user_request()
    request["fullName"] = None
    response = client.put("/users/3", json=request, headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 422

    request = get_alter_user_request()
    request["password"] = None
    response = client.put("/users/3", json=request, headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 422

    request = get_alter_user_request()
    request["role"] = None
    response = client.put("/users/3", json=request, headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 422

    request = get_alter_user_request()
    request["role"] = 1000
    response = client.put("/users/3", json=request, headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 422


def test_update_user__with_non_admin_user__returns_403(client: TestClient):
    request = get_alter_user_request()
    response = client.put("/users/3", json=request, headers=get_auth_headers(client, "pastor", "12345"))
    assert response.status_code == 403

    response = client.put("/users/3", json=request, headers=get_auth_headers(client, "readonly", "12345"))
    assert response.status_code == 403


def test_update_user__with_existing_username__returns_422(client: TestClient):
    request = get_alter_user_request()
    request["username"] = "pastor"  # Belongs to another user
    response = client.put("/users/3", json=request, headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 422
