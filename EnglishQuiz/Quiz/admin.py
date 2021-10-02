from django.contrib import admin
from Quiz.models import *
from nested_admin import NestedModelAdmin, NestedTabularInline
from django.forms import TextInput, Textarea
# Register your models here.

""" #Inline
class AnswerInline(admin.StackedInline):
    model = Answer
    max_num = 10
    extra = 0
class QuestionInline(admin.StackedInline):
    model = Question
    max_num = 10
    inlines = [AnswerInline]
    #ordering = ("question_order")
    extra = 0
 """

class AnswerInline(NestedTabularInline):
    model = Answer
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':50})},
    }

class QuestionInline(NestedTabularInline):
    model = Question
    extra = 0
    inlines = [AnswerInline]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':50})},
    }

class ExerciseAdmin(NestedModelAdmin):
    inlines = [
    QuestionInline
    ]

admin.site.register(Exercise,ExerciseAdmin)
""" 

#1
class ExerciseAd(admin.ModelAdmin):
    inlines = [QuestionInline,]
    list_display = ['title', 'time']
    search_fields = ['title', 'time']
admin.site.register(Exercise,ExerciseAd)
 """
#2
class QuestionAd(NestedModelAdmin):
    inlines = [AnswerInline,]
    list_display = ['id', 'description', 'time']
    search_fields = ['id', 'description', 'time']
admin.site.register(Question,QuestionAd)

#3
class AnswerAd(admin.ModelAdmin):
    list_display = ['id', 'question', 'description', 'is_correct']
    search_fields = ['id', 'description', 'is_correct']
admin.site.register(Answer,AnswerAd)

# #7
# class AssignmentAd(admin.ModelAdmin):
#     list_display = ['user', 'exercise', 'maximum','correct', 'date']
#     search_fields = ['user', 'exercise', 'maximum','correct']
# admin.site.register(Assignment,AssignmentAd)
