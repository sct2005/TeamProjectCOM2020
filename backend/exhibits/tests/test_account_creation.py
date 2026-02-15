import pytest
from django.contrib.auth.models import User
from django.urls import reverse

@pytest.mark.django_db
def test_signup_fails_without_password(client):
    response = client.post(reverse("signup"), {"username" : "Alice",
                                               "email" : "alice@example.com",
                                               "password1" : "",
                                               "password2" : ""})
    
    assert response.status_code == 200
    assert not User.objects.filter(username = "Alice").exists()

    form = response.context["form"]
    assert "password1" in form.errors

@pytest.mark.django_db
def test_signup_fails_without_username(client):
    response = client.post(reverse("signup"), {"username" : "",
                                               "email" : "alice@example.com",
                                               "password1" : "Password!",
                                               "password2" : "Password!"})
    
    assert response.status_code == 200
    assert not User.objects.filter(username = "").exists()

    form = response.context["form"]
    assert "username" in form.errors

@pytest.mark.django_db
def test_signup_fails_without_matching_passwords(client):
    response = client.post(reverse("signup"), {"username" : "Alice",
                                               "email" : "alice@example.com",
                                               "password1" : "Password!",
                                               "password2" : "Password123"})
    
    assert response.status_code == 200
    assert not User.objects.filter(username = "Alice").exists()


@pytest.mark.django_db
def test_signup_fails_with_duplicate_username(client):
    User.objects.create_user(username = "Alice", password = "Password!")

    response = client.post(reverse("signup"), {"username" : "Alice",
                                               "email" : "alice@example.com",
                                               "password1" : "Password!",
                                               "password2" : "Password!"})
    
    assert response.status_code == 200

    form = response.context["form"]
    assert "username" in form.errors
