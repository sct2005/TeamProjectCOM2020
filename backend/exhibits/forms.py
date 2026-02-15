from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class UsernameChangeForm(forms.Form):
    """Form to change the current user's username."""

    new_username = forms.CharField(
        max_length=150,
        label="New username",
        widget=forms.TextInput(attrs={"autocomplete": "username"}),
    )

    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        if user:
            self.fields["new_username"].initial = user.username

    def clean_new_username(self):
        username = self.cleaned_data.get("new_username", "").strip()
        if not username:
            raise forms.ValidationError("Username cannot be empty.")
        if User.objects.filter(username=username).exclude(pk=self.user.pk).exists():
            raise forms.ValidationError("This username is already in use.")
        return username
