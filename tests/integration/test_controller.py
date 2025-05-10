from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_country_name_endpoint():
    response = client.get("/api/country/us")
    assert response.status_code == 200
    data = response.json()
    assert "country" in data
    assert isinstance(data["country"], str)

def test_get_country_name_not_found():
    response = client.get("/api/country/zz")
    assert response.status_code == 404
    assert response.json()["detail"] == "Country code 'zz' not found"

def test_get_country_name_invalid_format():
    response = client.get("/api/country/1")
    assert response.status_code == 422
    data = response.json()
    assert data["detail"][0]["type"] == "string_pattern_mismatch"