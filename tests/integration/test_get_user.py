from fastapi.testclient import TestClient

def test_get_all__with_non_invalid_token__returns_403(client: TestClient):
    headers = {"Authorization": f"Bearer 123qweasd"}
    response = client.get("/users", headers=headers)
    assert response.status_code == 403


def test_get_all__with_non_admin_user__returns_403(client: TestClient):
    login_response = client.post("/login", data={"username": "pastor", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users", headers=headers)
    assert response.status_code == 403
    
    login_response = client.post("/login", data={"username": "readonly", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users", headers=headers)
    assert response.status_code == 403

def test_get_all__with_non_admin_user__returns_403(client: TestClient):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_get_user__with_invalid_token__returns_403(client: TestClient):
    headers = {"Authorization": "Bearer token_invalido"}
    response = client.get("/users/1", headers=headers)
    assert response.status_code == 403

def test_get_user__with_valid_token_admin__returns_200(client: TestClient):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/1", headers=headers)
    assert response.status_code == 200

def test_get_user__with_valid_token_and_readonly__returns_403(client: TestClient):
    login_response = client.post("/login", data={"username": "readonly", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/1", headers=headers)  # Trying to get the admin user
    assert response.status_code == 403

def test_get_user__with_valid_token_self__returns_200(client: TestClient):
    login_response = client.post("/login", data={"username": "readonly", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/3", headers=headers)
    assert response.status_code == 200

def test_get_user__with_user_not_found__returns_403(client: TestClient):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/1000", headers=headers)
    assert response.status_code == 403
