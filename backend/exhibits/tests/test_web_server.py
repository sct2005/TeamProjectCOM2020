import pytest
import time
from django.contrib.auth.models import User
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
def test_performance(client):
    start = time.time()
    response = client.get(reverse("home"))
    duration = time.time() - start
    assert duration < 1

@pytest.mark.django_db
def test_exhibits_page_loads(client):
    response = client.get(reverse("exhibits:list"))

    assert response.status_code == 200
    assert "Exhibits" in response.content.decode()

@pytest.mark.django_db
def test_signup_page_loads(client):
    response = client.get(reverse("signup"))

    assert response.status_code == 200
    assert "Create account" in response.content.decode()

@pytest.mark.django_db
def test_login_page_loads(client):
    response = client.get(reverse("login"))

    assert response.status_code == 200
    assert "Sign in" in response.content.decode()


