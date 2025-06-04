member_not_found = {
  "memberId": 100001,
  "ministrationDate": "2025-06-04",
  "worker1": "string",
  "worker2": "string",
  "isSharingTestimony": True,
  "isPublishingTestimony": True,
  "isPublishingTestimonyName": False,
  "isAgreedShareTestimony": False,
  "id": 1
}

member_with_dew_not_found = {
  "memberId": 101,
  "ministrationDate": "2025-06-04",
  "worker1": "string",
  "worker2": "string",
  "isSharingTestimony": True,
  "isPublishingTestimony": True,
  "isPublishingTestimonyName": False,
  "isAgreedShareTestimony": False,
  "id": 101
}

dew_found = {
  "memberId": 1,
  "ministrationDate": "2025-06-04",
  "worker1": "Jhon",
  "worker2": "Peter",
  "isSharingTestimony": True,
  "isPublishingTestimony": True,
  "isPublishingTestimonyName": False,
  "isAgreedShareTestimony": False,
  "id": 1
}

def test_find_member_dew_by_member_id__with_not_found_member_id__returns_404(client):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")
    response = client.get("/members/100000/dew",
                          headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 404

def test_find_dew_by_member_id__with_not_found_member_id__returns_404(client):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")
    response = client.get("/members/100000/dew",
                          headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 404

def test_find_dew_by_member_id__with_member_id__returns_200(client):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")
    response = client.get("/members/1/dew",
                          headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["memberId"] == 1

def test_create_dew__with_member_has_already_general__data_returns_409(client):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")
    create_response = client.post("/members/dew", json=dew_found,
                                  headers={"Authorization": f"Bearer {token}"})
    assert create_response.status_code == 409

def test_create_dew__with_member_not_found__returns_404(client):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")
    create_response = client.post("/members/dew", json=member_not_found,
                                  headers={"Authorization": f"Bearer {token}"})
    assert create_response.status_code == 404

def test_update_dew__with_member_not_found__returns_404(client):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")
    create_response = client.put("/members/dew", json=member_not_found,
                                 headers={"Authorization": f"Bearer {token}"})
    assert create_response.status_code == 404

def test_update_dew__with_member_has_not_dew__returns_404(client):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")
    create_response = client.put("/members/dew", json=member_with_dew_not_found,
                                 headers={"Authorization": f"Bearer {token}"})
    assert create_response.status_code == 404

def test_update_dew__with_member_ok__returns_200(client):
    login_response = client.post("/login", data={"username": "admin", "password": "12345"})
    token = login_response.headers.get("Authorization")
    create_response = client.put("/members/dew", json=dew_found,
                                 headers={"Authorization": f"Bearer {token}"})
    assert create_response.status_code == 200
    assert create_response.json()["memberId"] == 1
    assert create_response.json()["worker1"] == "Jhon"
    assert create_response.json()["worker2"] == "Peter"
    assert create_response.json()["isSharingTestimony"] == True
    assert create_response.json()["isPublishingTestimony"] == True
    assert create_response.json()["isAgreedShareTestimony"] == False
