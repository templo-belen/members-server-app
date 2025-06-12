from fastapi.testclient import TestClient

from tests.utils import get_auth_headers


def get_alter_user_request():
    return {
        "username": "username",
        "fullName": "John Doe",
        "password": "secret",
        "role": 1
    }

def test_create_user__with_invalid_token__returns_403(client: TestClient):
    headers = {"Authorization": f"Bearer 123qweasd"}
    response = client.post("/users", headers=headers)
    assert response.status_code == 403

def test_create_user__with_non_admin_user__returns_403(client: TestClient):
    response = client.post("/users", headers=get_auth_headers(client, "pastor", "12345"))
    assert response.status_code == 403

def test_create_user__with_invalid_request__returns_422(client: TestClient):
    request = get_alter_user_request()
    request["username"] = None
    response = client.post("/users", json=request, headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 422
    
    request = get_alter_user_request()
    request["fullName"] = None
    response = client.post("/users", json=request, headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 422
    
    request = get_alter_user_request()
    request["password"] = None
    response = client.post("/users", json=request, headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 422
    
    request = get_alter_user_request()
    request["role"] = None
    response = client.post("/users", json=request, headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 422
    
    request = get_alter_user_request()
    request["role"] = 1000
    response = client.post("/users", json=request, headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 422

def test_create_user__with_valid_request__returns_200(client: TestClient):
    request = get_alter_user_request()
    response = client.post("/users", json=request, headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 200

def test_create_user__with_existing_username__returns_422(client: TestClient):
    request = get_alter_user_request()
    request["username"] = "pastor" # Belongs to another user
    response = client.post("/users", json=request, headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 422
