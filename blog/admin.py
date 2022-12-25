from django.contrib import admin

# Register your models here.

from models import *


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(EducationalInstitution)
class EducationalInstitutionAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'country')
    list_filter = ('title', 'city', 'country')
    ordering = ('title', 'city', 'country')
    search_fields = ('title', 'city', 'country')


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'country')
    list_filter = ('title', 'city', 'country')
    ordering = ('title', 'city', 'country')
    search_fields = ('title', 'city', 'country')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'family_name', 'passport', 'city', 'country', 'education')
    list_filter = ('first_name', 'family_name', 'city', 'country', 'education')
    ordering = ('family_name', 'city', 'country', 'education')
    search_fields = ('first_name', 'family_name', 'city', 'country', 'education')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'family_name', 'passport', 'city', 'country', 'school')
    list_filter = ('first_name', 'family_name', 'city', 'country', 'school')
    ordering = ('family_name', 'city', 'country', 'school')
    search_fields = ('first_name', 'family_name', 'city', 'country', 'school')


