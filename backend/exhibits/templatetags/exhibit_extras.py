"""Template tags and filters for exhibits app."""

from django import template

register = template.Library()


@register.filter
def can_delete_comment(comment, user):
    """Check if user can delete this comment (own or admin)."""
    if not user or not user.is_authenticated:
        return False
    if comment.user_id == user.id:
        return True
    # Admin: UserProfile.access_level or Django superuser
    if getattr(user, "is_superuser", False):
        return True
    from .models import UserProfile
    try:
        profile = UserProfile.objects.get(user=user)
        return profile.is_admin
    except UserProfile.DoesNotExist:
        return False
