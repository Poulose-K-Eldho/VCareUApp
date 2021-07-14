from django.contrib import admin
from .models import Department,Doctor
# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Department,DepartmentAdmin)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name','age','email','available']
    list_editable = ['age','email','available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Doctor,DoctorAdmin)

