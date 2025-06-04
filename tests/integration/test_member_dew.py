def test_find_member_dew_by_member_id__with_not_found_member_id__returns_404(client):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")
    response = client.get("/members/100000/dew",
                          headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 404

