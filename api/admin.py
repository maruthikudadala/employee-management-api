# api/admin.py

from django.contrib import admin
from .models import Employee

# Register your model
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'role', 'date_joined')
    search_fields = ('name', 'email', 'department')
    list_filter = ('department', 'role', 'date_joined')