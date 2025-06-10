from fastapi.testclient import TestClient


def get_request():
    return {
        "currentPassword": "12345",
        "newPassword": "54321"
    }

def test_change_password__with_invalid_token__returns_403(client: TestClient):
    request = get_request()
    headers = {"Authorization": f"Bearer 123qweasd"}
    response = client.patch("/users/1/password", json=request, headers=headers)
    assert response.status_code == 403

def test_change_password__with_non_self_user__returns_403(client: TestClient):
    login_response = client.post("/login", data={"username": "pastor", "password": "12345"})
    token = login_response.headers.get("Authorization")

    request = get_request()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.patch("/users/3/password", json=request, headers=headers)
    assert response.status_code == 403

def test_change_password__with_bad_current_passoword__returns_422(client: TestClient):
    login_response = client.post("/login", data={"username": "pastor", "password": "12345"})
    token = login_response.headers.get("Authorization")

    request = get_request()
    request["currentPassword"] = "123qweasd"
    headers = {"Authorization": f"Bearer {token}"}
    response = client.patch("/users/2/password", json=request, headers=headers)
    assert response.status_code == 422

def test_change_password__with_valid_request__returns_200(client: TestClient):
    login_response = client.post("/login", data={"username": "pastor", "password": "12345"})
    token = login_response.headers.get("Authorization")

    request = get_request()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.patch("/users/2/password", json=request, headers=headers)
    assert response.status_code == 200
    
    login_response = client.post("/login", data={"username": "pastor", "password": request["newPassword"]})
    assert response.status_code == 200