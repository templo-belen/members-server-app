from fastapi.testclient import TestClient


def test_delete_user__with_admin_user__returns_200(client: TestClient):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.delete("/users/3", headers=headers)
    assert response.status_code == 200

def test_delete_user__with_non_admin_user__returns_403(client: TestClient):
    login_response = client.post("/login", data={"username": "pastor", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.delete("/users/3", headers=headers)
    assert response.status_code == 403

def test_delete_user__with_self_deleting__returns_422(client: TestClient):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.delete("/users/1", headers=headers)
    assert response.status_code == 422
