from django import forms
from .models import MeetingReport

class MeetingReportForm(forms.ModelForm):
    class Meta:
        model = MeetingReport
        fields = ['header', 'report_id', 'file', 'is_available']
