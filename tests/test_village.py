from fastapi.testclient import TestClient

from backend.app import app


def test_app_health():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
