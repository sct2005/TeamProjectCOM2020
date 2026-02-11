import pytest
import time
from django.contrib.auth.models import User
from django.urls import reverse

@pytest.mark.django_db
def test_sign_up_creates_user(client):
    response = client.post(reverse("signup"), {"username" : "Alice",
                                              "password1" : "Password!",
                                              "password2" : "Password!"})
    
    assert response.status_code == 302
    assert User.objects.filter(username="Alice").exists()

@pytest.mark.django_db
def test_successful_login(client, user):
    
    response = client.post(reverse("login"), {"username" : "Alice",
                                             "password" : "Password1"})
    
    assert response.status_code == 302

@pytest.mark.django_db
def test_invalid_password(client, user):
    response = client.post(reverse("login"), {"username" : "Alice",
                                              "password" : "WrongPassword!"})
    
    assert response.status_code == 200

@pytest.mark.django_db
def test_successful_logout(client):
    response = client.get(reverse("logout"))
    assert response.status_code == 302

@pytest.mark.django_db
def test_delete_account(client_log_in, user):
    response = client_log_in.post(reverse("profile_delete_account"))

    assert response.status_code == 302
    assert not user.__class__.objects.filter(username = "Alice").exists()

