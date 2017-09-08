from django.contrib import admin
from .models import Choice, Question

# Register your models here.

#tabularinline of django is the way it displays the tables
class ChoiceInline(admin.TabularInline):
    #show answer
    model = Choice

    #tree posible answers
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    #show question text, date published and recently published
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    #show panel filter
    list_filter = ['pub_date']

    #show panel search
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
