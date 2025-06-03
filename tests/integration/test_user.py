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
    login_response = client.post("/login", data={"username": "read", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/1", headers=headers)  # Trying to get the admin user
    assert response.status_code == 403

def test_get_user__with_user_not_found__returns_403(client):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/1000", headers=headers)
    assert response.status_code == 403
