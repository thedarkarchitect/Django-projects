from django.contrib import admin
from .models import Questions, Choices

# Register your models here.

admin.site.site_header = "VoteApp Amin"
admin.site.site_title = "VoteApp Admin Area"
admin.site.index_title = "Welcome to the VoteApp admin area"

class ChoiceInline(admin.TabularInline):
    model = Choices
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields' : ['question_text']}),
                    ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']})]
    inlines = [ChoiceInline]

# admin.site.register(Questions)
# admin.site.register(Choice)
admin.site.register(Questions, QuestionAdmin)