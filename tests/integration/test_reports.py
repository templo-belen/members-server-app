from sqlalchemy import text

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


def test_get_all_columns_success(client):
    response = client.get("/reports/columns", headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 200


def test_get_all_columns_forbidden(client):
    response = client.get("/reports/columns", headers=get_auth_headers(client, "pastor", "12345"))
    assert response.status_code == 403
