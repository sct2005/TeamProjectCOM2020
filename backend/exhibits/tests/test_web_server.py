import pytest
import requests
from django.urls import reverse


@pytest.mark.django_db
def test_health_endpoint(client):
    url = reverse("health")
    response = client.get(url)

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.django_db
def test_create_item(client):
    response = client.post(
        "/api/items/",
        data={"name": "Pen"},
        content_type = "application/json",
    )

    assert response.status_code == 201

def test_missing_field_returns_400(client):
    response = client.post("/api/items/", data = {})
    assert response.status_code == 400

def test_private_endpoint_unauthorised(client):
    response = client.get("/api/private/")
    assert response.status_code == 401

def test_live_api():
    r = requests.get("http://localhost:8000/health/")
    assert r.status_code == 200
