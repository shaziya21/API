from django.contrib import admin
from apii import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
