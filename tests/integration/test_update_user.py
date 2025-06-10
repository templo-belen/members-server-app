from fastapi.testclient import TestClient


def get_alter_user_request():
    return {
        "username": "username",
        "fullName": "John Doe",
        "password": "secret",
        "role": 1
    }

def test_update_user__with_valid_request__returns_200(client: TestClient):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")
    
    request = get_alter_user_request()
    request["username"] = "readonly"
    headers = {"Authorization": f"Bearer {token}"}
    response = client.put("/users/3", json=request, headers=headers)
    assert response.status_code == 200

def test_update_user__with_invalid_request__returns_422(client: TestClient):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")
    headers = {"Authorization": f"Bearer {token}"}
    
    request = get_alter_user_request()
    request["username"] = None
    response = client.put("/users/3", json=request, headers=headers)
    assert response.status_code == 422
    
    request = get_alter_user_request()
    request["fullName"] = None
    response = client.put("/users/3", json=request, headers=headers)
    assert response.status_code == 422
    
    request = get_alter_user_request()
    request["password"] = None
    response = client.put("/users/3", json=request, headers=headers)
    assert response.status_code == 422
    
    request = get_alter_user_request()
    request["role"] = None
    response = client.put("/users/3", json=request, headers=headers)
    assert response.status_code == 422
    
    request = get_alter_user_request()
    request["role"] = 1000
    response = client.put("/users/3", json=request, headers=headers)
    assert response.status_code == 422

def test_update_user__with_non_admin_user__returns_403(client: TestClient):
    login_response = client.post("/login", data={"username": "pastor", "password": "12345"})
    token = login_response.headers.get("Authorization")

    request = get_alter_user_request()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.put("/users/3", json=request, headers=headers)
    assert response.status_code == 403
    
    login_response = client.post("/login", data={"username": "readonly", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.put("/users/3", json=request, headers=headers)
    assert response.status_code == 403

def test_update_user__with_existing_username__returns_422(client: TestClient):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")

    request = get_alter_user_request()
    request["username"] = "pastor" # Belongs to another user
    headers = {"Authorization": f"Bearer {token}"}
    response = client.put("/users/3", json=request, headers=headers)
    assert response.status_code == 422
