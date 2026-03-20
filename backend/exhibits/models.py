from django.db import models
from django.conf import settings
import json

class Exhibit(models.Model):
    title = models.CharField(max_length=200, unique=True)
    domain = models.CharField(max_length=100)
    deployment_context = models.TextField()
    intended_use = models.TextField()

    system_type = models.CharField(max_length=100)
    inputs_and_assumptions = models.TextField()
    outputs_presented = models.TextField()

    failure_description = models.TextField()
    detection_method = models.TextField()
    affected_parties = models.TextField()

    contributing_factors = models.TextField()
    lessons_learned = models.TextField()
    image = models.ImageField(upload_to='exhibits/images/', blank=True, null=True, help_text="Image representing this exhibit")
    image_reference = models.CharField(max_length=200, blank=True, null=True, help_text="Reference/attribution for the image")
    supporting_artefacts = models.JSONField(default=list, blank=True, help_text="List of supporting artefact links")
    data_issues = models.TextField(blank=True, help_text="Data-related issues that contributed to the failure")
    technical_choices = models.TextField(blank=True, help_text="Technical choices that contributed to the failure")
    organizational_factors = models.TextField(blank=True, help_text="Organizational and governance factors")
    timeline = models.TextField(blank=True, help_text="Timeline of failure and aftermath")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Quiz(models.Model):
    exhibit = models.ForeignKey(
        Exhibit,
        on_delete=models.CASCADE,
        related_name="quizzes"
    )
    question = models.TextField()
    options = models.JSONField(default=list, help_text="List of multiple choice options", blank=True)
    correct_answer_index = models.IntegerField(default=0, help_text="Index of the correct answer in options list")
    explanation = models.TextField()

    def __str__(self):
        return f"Quiz for {self.exhibit.title}: {self.question[:30]}..."
    
    def get_correct_answer(self):
        """Returns the correct answer text"""
        if self.options and 0 <= self.correct_answer_index < len(self.options):
            return self.options[self.correct_answer_index]
        return ""


class Comment(models.Model):
    exhibit = models.ForeignKey(
        Exhibit,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="replies",
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        null=True,
        blank=True,
    )
    author_name = models.CharField(max_length=80)
    body = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        if self.parent_id:
            return f"Reply by {self.author_name} on {self.exhibit.title}"
        return f"Comment by {self.author_name} on {self.exhibit.title}"


class Bookmark(models.Model):
    """User bookmark of an exhibit."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookmarks",
    )
    exhibit = models.ForeignKey(
        Exhibit,
        on_delete=models.CASCADE,
        related_name="bookmarks",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "exhibit")

    def __str__(self):
        return f"Bookmark: {self.user} → {self.exhibit}"


class UserProfile(models.Model):
    """Extended profile for user (access level, etc.)."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    ACCESS_LEVELS = [
        ("admin", "Admin"),
        ("curator", "Curator"),
        ("user", "User"),
    ]
    access_level = models.CharField(
        max_length=20,
        choices=ACCESS_LEVELS,
        default="user",
    )

    def __str__(self):
        return f"Profile: {self.user.username} ({self.get_access_level_display()})"

    @property
    def is_admin(self):
        return self.access_level == "admin"

    @property
    def is_curator(self):
        """Curator or admin (admin inherits curator abilities)."""
        return self.access_level in ("admin", "curator")


class QuizScore(models.Model):
    """Per-user quiz performance for an exhibit (stores the best score)."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="quiz_scores",
    )
    exhibit = models.ForeignKey(
        Exhibit,
        on_delete=models.CASCADE,
        related_name="quiz_scores",
    )
    total_questions = models.PositiveIntegerField()
    correct_answers = models.PositiveIntegerField()
    score_percentage = models.FloatField()
    taken_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "exhibit")

    def __str__(self):
        return f"{self.user} – {self.exhibit} – {self.score_percentage:.1f}%"
