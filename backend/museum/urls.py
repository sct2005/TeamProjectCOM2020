"""
URL configuration for museum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from exhibits import views as exhibit_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", exhibit_views.home, name="home"),
    path("exhibits/", include("exhibits.urls")),
    path("health/", exhibit_views.health, name="health"),
    path("accounts/signup/", exhibit_views.signup, name="signup"),
    path("accounts/login/", exhibit_views.login_view, name="login"),
    path("accounts/logout/", exhibit_views.logout_view, name="logout"),
    path("accounts/profile/", exhibit_views.profile_view, name="profile"),
    path("accounts/profile/username/", exhibit_views.profile_change_username, name="profile_change_username"),
    path("accounts/profile/password/", exhibit_views.profile_change_password, name="profile_change_password"),
    path("accounts/profile/delete-scores/", exhibit_views.profile_delete_scores, name="profile_delete_scores"),
    path("accounts/profile/delete-account/", exhibit_views.profile_delete_account, name="profile_delete_account"),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

