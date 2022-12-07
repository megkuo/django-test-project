from django.contrib import admin

# Register your models here.

from .models import Choice, Question, DeepThought

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# written anytime you need to change the admin options for a model
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # first element of each tuple in fieldsets = title of the fieldset/section of fields
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

admin.site.register(DeepThought)

