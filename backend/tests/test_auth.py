import uuid
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    unique_username = f"testuser_{uuid.uuid4().hex[:8]}"
    response = client.post("/register", json={
        "username": unique_username,
        "password": "testpass"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"
def test_login():
    response=client.post("/login",json={
        "username":"testuser",
        "password":"testpass"

    })
    assert response.status_code == 200
    assert "access_token" in response.json()
def test_wrong_password():
    response=client.post("/login",json={
        "username":"testuser",
        "password":"wrongpassword"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Wrong Password"

   #assert - how u check 