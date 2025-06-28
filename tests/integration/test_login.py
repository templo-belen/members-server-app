from fastapi.testclient import TestClient


def login(client, username: str, password: str):
    return client.post("/login", data={"username": username, "password": password})


def test_login__with_invalid_user__returns_403(client: TestClient):
    login_response = login(client, "invalid", "12345")
    assert login_response.status_code == 401


def test_login__with_valid_user__returns_200(client: TestClient):
    login_response = login(client, "admin", "12345")

    print(login_response.json())

    assert login_response.status_code == 200
    assert login_response.headers.get("Authorization")
    assert login_response.json()["full_name"] == "Administrador Dominguez"
    assert login_response.json()["username"] == "admin"
    assert login_response.json()["features"] and len(login_response.json()["features"]) > 0
