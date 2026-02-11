import pytest
import time
from django.contrib.auth.models import User
from django.urls import reverse

@pytest.mark.django_db
def test_profile_page_requires_login(client):
    response = client.get(reverse("profile"))

    assert response.status_code == 302

@pytest.mark.django_db
def test_profile_page_loads(client_log_in):
    response = client_log_in.get(reverse("profile"))

    assert response.status_code == 200
    assert "Profile" in response.content.decode()