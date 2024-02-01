# ในไฟล์ forms.py หรือเพิ่มในไฟล์ models.py เพื่อให้เหมือนเดิม
from django import forms
from .models import Meeting

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'date', 'attendees', 'location']
