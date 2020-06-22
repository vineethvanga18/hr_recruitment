from django.contrib import admin
from .models import Application, Applicant


# Register your models here.

class ApplicationAdmin(admin.ModelAdmin):
    class Meta:
        model = Application


class ApplicantAdmin(admin.ModelAdmin):
    class Meta:
        model = Applicant


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Applicant, ApplicantAdmin)
