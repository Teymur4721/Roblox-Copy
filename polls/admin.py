from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # İlkin olaraq 3 boş cavab sətri göstərir

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    search_fields = ('question_text',)
    inlines = [ChoiceInline]