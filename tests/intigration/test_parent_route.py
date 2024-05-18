from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_parents():
    response = client.get("/parents")
    assert response.status_code == 200
    assert "status" in response.json()
    assert "meta" in response.json()
    assert "results" in response.json()
    assert "data" in response.json()