from django.db import models
import json

class Exhibit(models.Model):
    title = models.CharField(max_length=200)
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
