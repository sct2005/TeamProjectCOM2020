import pytest
import time
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect

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
    assert redirect("home")

@pytest.mark.django_db
def test_delete_account(client_log_in, user):
    response = client_log_in.post(reverse("profile_delete_account"))

    assert response.status_code == 302
    assert not user.__class__.objects.filter(username = "Alice").exists()

@pytest.mark.django_db
def test_successful_change_password(logged_in_client, user):
    response = logged_in_client.post(reverse("profile_change_password"),{"old_password": "Password1",
                                                                         "new_password1": "NewPassword123!",
                                                                         "new_password2": "NewPassword123!",})
    
    assert response.status_code == 302

    user.refresh_from_db()
    assert user.check_password("NewPassword123")

@pytest.mark.django_db
def test_unsuccessful_change_password_old_password_does_not_match(logged_in_client, user):
    response = logged_in_client.post(reverse("profile_change_password"),{"old_password": "UnmatchedPassword",
                                                                         "new_password1": "NewPassword123!",
                                                                         "new_password2": "NewPassword123!"})
    
    assert response.status_code == 200

def test_unsuccessful_change_password_passwords_do_not_match(logged_in_client, user):
    response = logged_in_client.post(reverse("profile_change_password"),{"old_password": "Password1",
                                                                         "new_password1": "NewPassword123!",
                                                                         "new_password2": "UnmatchedPassword"})
    
    assert response.status_code == 200

@pytest.mark.django_db
def test_successful_change_username(logged_in_client, user):
    response = logged_in_client.post(reverse("profile_change_username"), {"new_username" : "Bob"})

    assert response.status_code == 302

@pytest.mark.django_db
def test_unsuccessful_change_username_username_taken(logged_in_client, user):
    User.objects.create_user(username = "Bob", password = "Password!")

    response = logged_in_client.post(reverse("profile_change_username"), {"new_username" : "Bob"})

    assert response.status_code == 200

@pytest.mark.django_db
def test_unsuccessful_change_username_username_empty(logged_in_client, user):
    response = logged_in_client.post(reverse("profile_change_username"), {"new_username" : ""})

    assert response.status_code == 200

