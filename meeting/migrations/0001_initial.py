# Generated by Django 4.2.6 on 2024-02-01 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('meeting_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('attendees', models.TextField(blank=True)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
    ]
