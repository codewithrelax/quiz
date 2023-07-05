from django.contrib import admin
from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_name', 'option1','option2','option3','option4',correct_option')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

