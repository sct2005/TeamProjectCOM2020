from django.contrib import admin
from .models import Exhibit, Quiz

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
