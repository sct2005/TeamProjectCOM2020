"""RBAC decorators for admin, curator, and user access control."""

from functools import wraps
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages


def _get_user_profile(user):
    """Get or create UserProfile for user."""
    from .models import UserProfile
    profile, _ = UserProfile.objects.get_or_create(user=user, defaults={"access_level": "user"})
    return profile


def admin_required(view_func):
    """Decorator: user must be admin or redirect with error."""

    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        profile = _get_user_profile(request.user)
        if not profile.is_admin:
            messages.error(request, "You do not have permission to access this page.")
            return redirect("profile")
        return view_func(request, *args, **kwargs)

    return login_required(_wrapped)


def curator_required(view_func):
    """Decorator: user must be curator or admin."""

    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        profile = _get_user_profile(request.user)
        if not profile.is_curator:
            messages.error(request, "You do not have permission to access this page.")
            return redirect("profile")
        return view_func(request, *args, **kwargs)

    return login_required(_wrapped)


def can_delete_comment(user, comment):
    """Check if user can delete a comment (own comment or admin)."""
    if not user.is_authenticated:
        return False
    if comment.user_id == user.id:
        return True
    # Admin: UserProfile.access_level or Django superuser
    if getattr(user, "is_superuser", False):
        return True
    profile = _get_user_profile(user)
    return profile.is_admin
