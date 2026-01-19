from django.urls import path
from . import views

urlpatterns = [
    path("", views.exhibit_list, name="exhibit_list"),
    path("<int:exhibit_id>/", views.exhibit_detail, name="exhibit_detail"),
]
