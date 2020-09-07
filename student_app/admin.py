from django.contrib import admin
from .models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','income']

admin.site.register(Student, StudentAdmin)
