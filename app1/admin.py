from django.contrib import admin

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields=['date', 'text']

admin.site.register(Question)
# Register your models here.
