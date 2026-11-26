from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Doctor, Patient, Specialty

admin.site.register(User, UserAdmin)
admin.site.register(Specialty)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return ('license_number',) if obj else ()

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return ('national_id',) if obj else ()