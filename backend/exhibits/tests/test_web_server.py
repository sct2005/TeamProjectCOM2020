import pytest
import json
import requests
from django.urls import reverse


@pytest.mark.django_db
def test_health_endpoint(client):
    url = reverse("health")
    response = client.get(url)

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.django_db
def test_home_page_loads(client):
    response = client.get(reverse("home"))

    assert response.status_code == 200

@pytest.mark.django_db
def test_exhibits_page_loads(client):
    response = client.get(reverse("list"))

    assert response.status_code == 200


