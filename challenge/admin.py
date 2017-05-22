from django.contrib import admin
from challenge.models import Question
from challenge.models import Winner
from django.forms import TextInput
from django.db import models


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('disp_no',
                    'title',
                    'genre',
                    'point',
                    'status',
                    'created_at',
                    'updated_at')
    list_display_links = ('title', )
    list_filter = ('genre',
                   'point',
                   'created_at',
                   'updated_at')
    search_fields = ('title', )
    ordering = ('disp_no', )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(
                           attrs={'size': 80, })},
    }

class WinnerAdmin(admin.ModelAdmin):
    list_display = ('question', 'name', )
    ordering = ('id',)
    list_display_links = ('name', )
    list_filter = ('question', )
    search_fields = ('name', 'question__title', )

admin.site.register(Question, QuestionAdmin)
admin.site.register(Winner, WinnerAdmin)

admin.site.site_header = 'CTF Manager'
