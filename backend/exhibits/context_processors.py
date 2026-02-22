"""Context processors for templates."""

def user_profile(request):
    """Add user_profile to template context for authenticated users."""
    if request.user.is_authenticated:
        from .models import UserProfile
        profile, _ = UserProfile.objects.get_or_create(user=request.user, defaults={"access_level": "user"})
        return {"user_profile": profile}
    return {"user_profile": None}
