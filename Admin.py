from django.contrib import admin
from .models import Question, Choice, Vote

class ChoiceInline(admin.TabularInline):
   model = Choice
   extra = 2  # Number of empty choice fields to display

class QuestionAdmin(admin.ModelAdmin):
   fieldsets = [
      (None, {'fields': ['question_text']}),
      ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
   ]
   inlines = [ChoiceInline]
   list_display = ('question_text', 'pub_date')
   list_filter = ['pub_date']
   search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
   list_display = ('choice_text', 'votes', 'question')
   list_filter = ['question']
   search_fields = ['choice_text']

class VoteAdmin(admin.ModelAdmin):
   list_display = ('voter_name', 'choice')
   list_filter = ['choice']
   search_fields = ['voter_name']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Vote, VoteAdmin)