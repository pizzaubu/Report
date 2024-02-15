from django.db import models
from accounts.models import User


class MeetingReport(models.Model):
    header = models.CharField(max_length=20)
    report_id = models.CharField(max_length=20)
    file = models.FileField(upload_to='reports/')
    is_available = models.BooleanField(default=True)

class MyFiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='files')
    file = models.FileField(upload_to='user_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"File uploaded by {self.user.username} on {self.uploaded_at}"
