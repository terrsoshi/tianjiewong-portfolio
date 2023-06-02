from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date')
    search_fields = ('title', 'description', 'skills__name',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_per_page = 10

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'institution','start_date', 'end_date')
    search_fields = ('title', 'description', 'location', 'institution', 'skills__name')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title','institution','start_date', 'end_date')
    search_fields = ('title', 'description', 'location', 'institution', 'subjects__name')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester')
    search_fields = ('name',)
    list_per_page = 10

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('number', 'education', 'start_date', 'end_date')
    search_fields = ('number', 'education')

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at')