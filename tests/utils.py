def get_auth_headers(client, username: str, password: str):
    login_response = client.post("/login", data={"username": username, "password": password})

    assert login_response.status_code == 200

    token = login_response.headers.get("Authorization")

    assert token is not None

    return {"Authorization": f"Bearer {token}"}
