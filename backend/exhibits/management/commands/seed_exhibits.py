import json
import os
import hashlib
from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings
from exhibits.models import Exhibit, Quiz

class Command(BaseCommand):
    help = "Seed the database with exhibits and quizzes"

    def handle(self, *args, **kwargs):
        # Repo root (2 levels above 'backend' folder)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        # BASE_DIR now = /workspaces/TeamProjectCOM2020

        exhibits_path = os.path.join(BASE_DIR, "data", "seed", "exhibits.json")
        quizzes_path = os.path.join(BASE_DIR, "data", "seed", "quizzes.json")
        
        # Get the media root path for images
        # Use Django's MEDIA_ROOT setting, or fall back to default location
        if hasattr(settings, 'MEDIA_ROOT') and settings.MEDIA_ROOT:
            media_root = os.path.join(settings.MEDIA_ROOT, "exhibits", "images")
        else:
            # Fallback to default location
            media_root = os.path.join(BASE_DIR, "backend", "media", "exhibits", "images")

        # Load Exhibits
        with open(exhibits_path, "r") as f:
            exhibits_data = json.load(f)

        # Remove exhibits not in the seed file (replace mode: DB reflects seed)
        seed_titles = [ex["title"] for ex in exhibits_data]
        deleted_count, _ = Exhibit.objects.exclude(title__in=seed_titles).delete()
        if deleted_count:
            self.stdout.write(self.style.WARNING(f"Removed {deleted_count} exhibit(s) no longer in seed."))

        for ex_data in exhibits_data:
            # Extract image_filename if present
            image_filename = ex_data.pop("image_filename", None)
            # Also remove old image_url field if present
            ex_data.pop("image_url", None)
            
            # Filter out image field if it exists (we'll handle it separately)
            exhibit_data = {k: v for k, v in ex_data.items() if k != "image"}
            
            ex, created = Exhibit.objects.get_or_create(
                title=ex_data["title"],
                defaults=exhibit_data
            )
            
            # Handle image assignment if filename is provided
            if image_filename:
                image_path = os.path.join(media_root, image_filename)
                if os.path.exists(image_path):
                    # Calculate hash of source file to compare with existing image
                    def get_file_hash(filepath):
                        """Calculate MD5 hash of a file"""
                        hash_md5 = hashlib.md5()
                        with open(filepath, 'rb') as f:
                            for chunk in iter(lambda: f.read(4096), b""):
                                hash_md5.update(chunk)
                        return hash_md5.hexdigest()
                    
                    source_hash = get_file_hash(image_path)
                    
                    # Check if exhibit already has this exact image assigned
                    image_already_assigned = False
                    if ex.image:
                        try:
                            current_image_path = ex.image.path
                            if os.path.exists(current_image_path):
                                current_hash = get_file_hash(current_image_path)
                                if current_hash == source_hash:
                                    image_already_assigned = True
                        except:
                            # If we can't access the path, check by base filename
                            current_image_name = os.path.basename(ex.image.name)
                            base_name = os.path.splitext(image_filename)[0]
                            current_base = os.path.splitext(current_image_name)[0]
                            if current_base == base_name or current_base.startswith(base_name + '_'):
                                image_already_assigned = True
                    
                    if not image_already_assigned:
                        # Delete old image file if it exists and is different
                        if ex.image:
                            try:
                                old_path = ex.image.path
                                if os.path.exists(old_path):
                                    old_hash = get_file_hash(old_path)
                                    if old_hash != source_hash:
                                        os.remove(old_path)
                            except:
                                pass  # Ignore errors when deleting old file
                        
                        with open(image_path, 'rb') as img_file:
                            ex.image.save(image_filename, File(img_file), save=True)
                        self.stdout.write(f"  → Assigned image: {image_filename}")
                    else:
                        self.stdout.write(f"  ✓ Image already assigned: {image_filename}")
                else:
                    self.stdout.write(self.style.WARNING(f"  ⚠ Image not found: {image_filename} (skipping)"))
            
            if created:
                self.stdout.write(f"Created Exhibit: {ex.title}")
            else:
                # Update existing exhibit
                for key, value in exhibit_data.items():
                    setattr(ex, key, value)
                ex.save()
                self.stdout.write(f"Updated Exhibit: {ex.title}")

        # Load Quizzes
        with open(quizzes_path, "r") as f:
            quizzes_data = json.load(f)

        # Build set of (exhibit_title, question) that are in JSON so we can remove DB questions no longer in JSON
        questions_in_json = {}  # exhibit_title -> set of question strings
        for q_data in quizzes_data:
            title = q_data["exhibit_title"]
            questions_in_json.setdefault(title, set()).add(q_data["question"])

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

        # Remove quiz questions that are no longer in the JSON (sync with seed data)
        for ex_data in exhibits_data:
            exhibit = Exhibit.objects.get(title=ex_data["title"])
            allowed_questions = questions_in_json.get(exhibit.title, set())
            to_remove = Quiz.objects.filter(exhibit=exhibit).exclude(question__in=allowed_questions)
            removed_count = to_remove.count()
            if removed_count:
                to_remove.delete()
                self.stdout.write(self.style.WARNING(f"Removed {removed_count} quiz question(s) from {exhibit.title}"))
