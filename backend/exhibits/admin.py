from django.contrib import admin
from .models import Exhibit, Quiz, Comment, UserProfile

@admin.register(Exhibit)
class ExhibitAdmin(admin.ModelAdmin):
    list_display = ['title', 'domain', 'created_at']
    list_filter = ['domain', 'created_at']
    search_fields = ['title', 'domain']
    readonly_fields = ['created_at']

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['exhibit', 'question', 'correct_answer_index']
    list_filter = ['exhibit']
    search_fields = ['question', 'exhibit__title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["exhibit", "author_name", "parent", "created_at"]
    list_filter = ["exhibit", "created_at"]
    search_fields = ["author_name", "body", "exhibit__title"]
    readonly_fields = ["created_at"]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "access_level"]
    list_filter = ["access_level"]
    search_fields = ["user__username"]
