from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
]
