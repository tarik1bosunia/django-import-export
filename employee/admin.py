from django.contrib import admin

from employee.models import Employee

from import_export.admin import ImportExportModelAdmin

admin.site.register(Employee, ImportExportModelAdmin)

# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ['id', 'first_name', 'last_name', 'age', 'monthly_salary']
