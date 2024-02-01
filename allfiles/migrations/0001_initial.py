# Generated by Django 4.2.6 on 2024-02-01 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=20)),
                ('report_id', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to='reports/')),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]
