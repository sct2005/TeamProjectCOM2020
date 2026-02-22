from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

from .models import Exhibit, Quiz, UserProfile


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


class UserRoleForm(forms.Form):
    """Form for admin to change a user's role."""

    access_level = forms.ChoiceField(
        choices=UserProfile.ACCESS_LEVELS,
        label="Role",
    )


class ExhibitForm(forms.ModelForm):
    """Form for creating/editing exhibits (curator)."""

    class Meta:
        model = Exhibit
        fields = [
            "title", "domain", "deployment_context", "intended_use",
            "system_type", "inputs_and_assumptions", "outputs_presented",
            "failure_description", "detection_method", "affected_parties",
            "contributing_factors", "lessons_learned",
            "image", "image_reference",
            "supporting_artefacts", "data_issues", "technical_choices",
            "organizational_factors", "timeline",
        ]


class QuizForm(forms.ModelForm):
    """Form for creating/editing quiz questions."""

    options_text = forms.CharField(
        required=False,
        label="Options (one per line)",
        widget=forms.Textarea(attrs={"rows": 4}),
        help_text="Enter each option on a new line. The first line is the correct answer by default.",
    )

    class Meta:
        model = Quiz
        fields = ["question", "explanation"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.options:
            self.fields["options_text"].initial = "\n".join(self.instance.options)
            # Store correct index for display
            self._correct_index = self.instance.correct_answer_index

    def clean_options_text(self):
        text = self.cleaned_data.get("options_text", "").strip()
        if not text:
            return []
        options = [line.strip() for line in text.split("\n") if line.strip()]
        return options

    def save(self, commit=True):
        quiz = super().save(commit=False)
        options = self.cleaned_data.get("options_text") or []
        quiz.options = options
        quiz.correct_answer_index = 0
        if commit:
            quiz.save()
        return quiz
