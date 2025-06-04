from fastapi.testclient import TestClient

def test_get_all__with_non_invalid_token__returns_403(client):
    headers = {"Authorization": f"Bearer 123qweasd"}
    response = client.get("/users", headers=headers)
    assert response.status_code == 403


def test_get_all__with_non_admin_user__returns_403(client):
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

def test_get_all__with_non_admin_user__returns_403(client):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_get_user__with_invalid_token__returns_403(client):
    headers = {"Authorization": "Bearer token_invalido"}
    response = client.get("/users/1", headers=headers)
    assert response.status_code == 403

def test_get_user__with_valid_token_admin__returns_200(client):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/1", headers=headers)
    assert response.status_code == 200

def test_get_user__with_valid_token_and_readonly__returns_403(client):
    login_response = client.post("/login", data={"username": "readonly", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/1", headers=headers)  # Trying to get the admin user
    assert response.status_code == 403

def test_get_user__with_valid_token_self__returns_200(client):
    login_response = client.post("/login", data={"username": "readonly", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/3", headers=headers)
    assert response.status_code == 200

def test_get_user__with_user_not_found__returns_403(client):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/1000", headers=headers)
    assert response.status_code == 403

def test_create_user__with_invalid_token__returns_403(client):
    headers = {"Authorization": f"Bearer 123qweasd"}
    response = client.post("/users", headers=headers)
    assert response.status_code == 403

def test_create_user__with_non_admin_user__returns_403(client):
    login_response = client.post("/login", data={"username": "pastor", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/users", headers=headers)
    assert response.status_code == 403

def test_create_user__with_valid_request__returns_200(client: TestClient):
    def get_request():
        return {
            "username": "username",
            "fullName": "John Doe",
            "fullName": "John Doe",
            "password": "secret",
            "role": 1
        }
    
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")
    headers = {"Authorization": f"Bearer {token}"}
    
    request = get_request()
    request["username"] = None
    response = client.post("/users", json=request, headers=headers)
    assert response.status_code == 422
    
    request = get_request()
    request["username"] = None
    response = client.post("/users", json=request, headers=headers)
    assert response.status_code == 422
    
    request = get_request()
    request["fullName"] = None
    response = client.post("/users", json=request, headers=headers)
    assert response.status_code == 422
    
    request["password"] = None
    response = client.post("/users", json=request, headers=headers)
    assert response.status_code == 422
    
    request["password"] = None
    request["role"] = None
    response = client.post("/users", json=request, headers=headers)
    assert response.status_code == 422
    
    request["password"] = None
    request["role"] = 1000
    response = client.post("/users", json=request, headers=headers)
    assert response.status_code == 422

def test_create_user__with_valid_request__returns_422(client: TestClient):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")
    
    request = {
        "username": "username",
        "fullName": "John Doe",
        "fullName": "John Doe",
        "password": "secret",
        "role": 1
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/users", json=request, headers=headers)
    assert response.status_code == 200

def test_create_user__with_existing_username__returns_422(client: TestClient):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")
    
    request = {
        "username": "admin",
        "fullName": "John Doe",
        "fullName": "John Doe",
        "password": "secret",
        "role": 1
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/users", json=request, headers=headers)
    assert response.status_code == 422

