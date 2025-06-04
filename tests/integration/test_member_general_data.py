from tests.utils import get_auth_headers

def test_find_general_data_by_member_id__with_not_found_member_id__returns_404(client):
    response = client.get("/members/100000/general-data",
                          headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 404

def test_find_general_data_by_member_id__with_member_id__returns_200(client):
    response = client.get("/members/1/general-data",
                          headers=get_auth_headers(client, "admin", "12345"))
    assert response.status_code == 200
    assert response.json()["memberId"] == 1

def test_create_general_data__with_member_has_already_general__data_returns_409(client):
    create_response = client.post("/members/1/general-data", json={
      "memberId": 1,
      "conversionDate": "2025-06-04",
      "conversionPlace": "string",
      "baptismDate": "2025-06-04",
      "baptismPlace": "string",
      "baptismHolySpiritDate": "2025-06-04",
      "baptismHolySpiritPlace": "string",
      "baptismPastorName": "string",
      "baptismDenomination": "string",
      "activeMemberSince": "2025-06-04",
      "leavingReason": "enfermedad",
      "leavingReasonDescription": "string",
      "leavingDate": "2025-06-04",
      "acceptanceComment": "string"
    }, headers=get_auth_headers(client, "admin", "12345"))
    assert create_response.status_code == 409

def test_create_general_data__with_member_not_found__returns_404(client):
    create_response = client.post("/members/1000/general-data", json={
      "memberId": 1000,
      "conversionDate": "2025-06-04",
      "conversionPlace": "string",
      "baptismDate": "2025-06-04",
      "baptismPlace": "string",
      "baptismHolySpiritDate": "2025-06-04",
      "baptismHolySpiritPlace": "string",
      "baptismPastorName": "string",
      "baptismDenomination": "string",
      "activeMemberSince": "2025-06-04",
      "leavingReason": "enfermedad",
      "leavingReasonDescription": "string",
      "leavingDate": "2025-06-04",
      "acceptanceComment": "string"
    }, headers=get_auth_headers(client, "admin", "12345"))
    assert create_response.status_code == 404

def test_update_general_data__with_member_not_found__returns_404(client):
    create_response = client.put("/members/1000/general-data", json={
      "id": 1000,
      "memberId": 1000,
      "conversionDate": "2025-06-04",
      "conversionPlace": "string",
      "baptismDate": "2025-06-04",
      "baptismPlace": "string",
      "baptismHolySpiritDate": "2025-06-04",
      "baptismHolySpiritPlace": "string",
      "baptismPastorName": "string",
      "baptismDenomination": "string",
      "activeMemberSince": "2025-06-04",
      "leavingReason": "enfermedad",
      "leavingReasonDescription": "string",
      "leavingDate": "2025-06-04",
      "acceptanceComment": "string"
    }, headers=get_auth_headers(client, "admin", "12345"))
    assert create_response.status_code == 404

def test_update_general_data__with_member_has_not_general_data__returns_404(client):
    create_response = client.put("/members/101/general-data", json={
      "id": 101,
      "memberId": 101,
      "conversionDate": "2025-06-04",
      "conversionPlace": "string",
      "baptismDate": "2025-06-04",
      "baptismPlace": "string",
      "baptismHolySpiritDate": "2025-06-04",
      "baptismHolySpiritPlace": "string",
      "baptismPastorName": "string",
      "baptismDenomination": "string",
      "activeMemberSince": "2025-06-04",
      "leavingReason": "enfermedad",
      "leavingReasonDescription": "string",
      "leavingDate": "2025-06-04",
      "acceptanceComment": "string"
    }, headers=get_auth_headers(client, "admin", "12345"))
    assert create_response.status_code == 404

def test_update_general_data__with_member_ok__returns_200(client):
    create_response = client.put("/members/1/general-data", json={
      "id": 1,
      "memberId": 1,
      "conversionDate": "2025-06-04",
      "conversionPlace": "string",
      "baptismDate": "2025-06-04",
      "baptismPlace": "string",
      "baptismHolySpiritDate": "2025-06-04",
      "baptismHolySpiritPlace": "string",
      "baptismPastorName": "string",
      "baptismDenomination": "string",
      "activeMemberSince": "2025-06-04",
      "leavingReason": "enfermedad",
      "leavingReasonDescription": "My leaving reason",
      "leavingDate": "2025-06-04",
      "acceptanceComment": "string"
    }, headers=get_auth_headers(client, "admin", "12345"))
    assert create_response.status_code == 200
    assert create_response.json()["memberId"] == 1
    assert create_response.json()["leavingReasonDescription"] == "My leaving reason"
