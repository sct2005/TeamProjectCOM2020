from django.urls import path
from . import views

app_name = "exhibits"

urlpatterns = [
    path("", views.exhibit_list, name="list"),
    path("<int:pk>/", views.exhibit_detail, name="detail"),
    path("<int:pk>/quiz/", views.quiz_view, name="quiz"),
]
