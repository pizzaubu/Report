# allfiles/admins.py
from django.contrib import admin
from .models import MeetingReport

class MeetingReportAdmin(admin.ModelAdmin):
    list_display = ('header', 'report_id', 'file', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('header', 'report_id')

admin.site.register(MeetingReport, MeetingReportAdmin)
