# ในไฟล์ urls.py ของแอปหรือโปรเจค
from django.urls import path
from .views import create_meeting

urlpatterns = [
    path('create_meeting/', create_meeting, name='create_meeting'),
    # เพิ่ม URL pattern ต่อไปตามที่ต้องการ
]
