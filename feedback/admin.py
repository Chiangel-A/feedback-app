from django.contrib import admin
from .models import Course, Entreprenuership, Ict, Subject, Profile


# Register your models here.


admin.site.register(Subject)


@admin.register(Course)
class Course(admin.ModelAdmin):
	list_display = ['name', 'facilitator', 'subject']


@admin.register(Entreprenuership)
class e_feedback(admin.ModelAdmin):
	list_display = ['course_title',]

@admin.register(Ict)
class ict_feedback(admin.ModelAdmin):
	list_display = ['course_title',]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['gender','phone_number', 'home_address']

# admin.site.register(Profile, ProfileAdmin)


