from django.contrib import admin

from .models import (
    Instructor,
    Learner,
    Course,
    Lesson,
    Enrollment,
    Question,
    Choice,
    Submission
)


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']


admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
