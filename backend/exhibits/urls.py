from django.urls import path
from . import views

app_name = "exhibits"

urlpatterns = [
    path("", views.exhibit_list, name="list"),
    path("create/", views.exhibit_create, name="create"),
    path("<int:pk>/", views.exhibit_detail, name="detail"),
    path("<int:pk>/edit/", views.exhibit_edit, name="edit"),
    path("<int:pk>/delete/", views.exhibit_delete, name="delete"),
    path("<int:pk>/comments/post/", views.post_comment, name="post_comment"),
    path(
        "<int:pk>/comments/<int:comment_id>/delete/",
        views.delete_comment,
        name="delete_comment",
    ),
    path("<int:pk>/quiz/", views.quiz_view, name="quiz"),
    path("<int:pk>/quiz/manage/", views.quiz_manage, name="quiz_manage"),
    path("<int:pk>/quiz/add/", views.quiz_add, name="quiz_add"),
    path("<int:pk>/quiz/<int:quiz_id>/edit/", views.quiz_edit, name="quiz_edit"),
    path("<int:pk>/quiz/<int:quiz_id>/delete/", views.quiz_delete, name="quiz_delete"),
]

