"""Management command to promote a user to admin role."""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from exhibits.models import UserProfile

User = get_user_model()


class Command(BaseCommand):
    help = "Set a user's role to admin (usage: python manage.py set_admin <username>)"

    def add_arguments(self, parser):
        parser.add_argument("username", type=str, help="Username to promote to admin")

    def handle(self, *args, **options):
        username = options["username"]
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"User '{username}' not found."))
            return
        profile, _ = UserProfile.objects.get_or_create(user=user, defaults={"access_level": "user"})
        profile.access_level = "admin"
        profile.save()
        self.stdout.write(self.style.SUCCESS(f"User '{username}' is now an admin."))
