import pytest
from django.contrib.auth.models import User

@pytest.fixture
def user(db):
    return User.objects.create_user(username = "Alice",
                                    email = "alice@example.com",
                                    password = "Password1")

@pytest.fixture
def client_log_in(client, user):
    client.login(username = "Alice", password = "Password1")
    return client
