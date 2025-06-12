from fastapi.testclient import TestClient

from tests.utils import get_auth_headers


def test_delete_user__with_admin_user__returns_200(client: TestClient):
    response = client.delete("/users/3", headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 200


def test_delete_user__with_non_admin_user__returns_403(client: TestClient):
    response = client.delete("/users/3", headers=get_auth_headers(client, "pastor", "12345"))
    assert response.status_code == 403


def test_delete_user__with_self_deleting__returns_422(client: TestClient):
    response = client.delete("/users/1", headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 422
