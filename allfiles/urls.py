# report/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create_report/',views.create_report, name='create_report'),
    path('edit_report/<int:report_id>/', views.edit_report, name='edit_report'),
    path('view_reports/', views.view_reports, name='view_reports'),
]
