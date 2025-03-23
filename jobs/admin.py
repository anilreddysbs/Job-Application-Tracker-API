from django.contrib import admin

# Register your models here.
from .models import JobApplication


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'application_date', 'status', 'notes')
    list_filter = ('status', 'application_date')
    search_fields = ('job_title', 'company_name')