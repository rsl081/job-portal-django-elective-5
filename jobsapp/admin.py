from django.contrib import admin
from .models import User, Job, Applicant
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = 'Admin Job Portal'


class JobPortalUser(admin.ModelAdmin):
    exclude = ('groups', 'password', 'user_permissions',)
    list_filter = ('role', 'last_login', 'date_joined', 'is_active',)


class JobPortalApplicant(admin.ModelAdmin):
    list_filter = ('job',)


class JobPortalJobs(admin.ModelAdmin):
    list_filter = ('category', 'type', 'company_name', 'user', 'last_date', 'created_at')


admin.site.register(User, JobPortalUser)
admin.site.register(Job, JobPortalJobs)
admin.site.register(Applicant, JobPortalApplicant)
admin.site.unregister(Group)
