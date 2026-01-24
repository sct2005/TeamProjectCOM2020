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
