from django.contrib import admin
from .models import Company, Employee, Department
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'company_ended']
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee)
admin.site.register(Department)
