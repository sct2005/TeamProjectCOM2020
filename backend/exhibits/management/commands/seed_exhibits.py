import json
import os
from django.core.management.base import BaseCommand
from exhibits.models import Exhibit, Quiz

class Command(BaseCommand):
    help = "Seed the database with exhibits and quizzes"

    def handle(self, *args, **kwargs):
        # Repo root (2 levels above 'backend' folder)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        # BASE_DIR now = /workspaces/TeamProjectCOM2020

        exhibits_path = os.path.join(BASE_DIR, "data", "seed", "exhibits.json")
        quizzes_path = os.path.join(BASE_DIR, "data", "seed", "quizzes.json")

        # Load Exhibits
        with open(exhibits_path, "r") as f:
            exhibits_data = json.load(f)

        for ex_data in exhibits_data:
            ex, created = Exhibit.objects.get_or_create(
                title=ex_data["title"],
                defaults=ex_data
            )
            if created:
                self.stdout.write(f"Created Exhibit: {ex.title}")
            else:
                # Update existing exhibit
                for key, value in ex_data.items():
                    setattr(ex, key, value)
                ex.save()
                self.stdout.write(f"Updated Exhibit: {ex.title}")

        # Load Quizzes
        with open(quizzes_path, "r") as f:
            quizzes_data = json.load(f)

        for q_data in quizzes_data:
            exhibit = Exhibit.objects.get(title=q_data["exhibit_title"])
            quiz, created = Quiz.objects.get_or_create(
                exhibit=exhibit,
                question=q_data["question"],
                defaults={
                    "options": q_data.get("options", []),
                    "correct_answer_index": q_data.get("correct_answer_index", 0),
                    "explanation": q_data.get("explanation", "")
                }
            )
            if created:
                self.stdout.write(f"Created Quiz: {quiz.question[:30]}...")
            else:
                # Update existing quiz
                quiz.options = q_data.get("options", [])
                quiz.correct_answer_index = q_data.get("correct_answer_index", 0)
                quiz.explanation = q_data.get("explanation", "")
                quiz.save()
                self.stdout.write(f"Updated Quiz: {quiz.question[:30]}...")
