from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=255)
    meeting_id = models.AutoField(primary_key=True)
    date = models.DateField()
    attendees = models.TextField(blank=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title
