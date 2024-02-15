from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm
from .models import UserManager
from allfiles.models import MyFiles

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')  
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        try:
            UserManager().reset_password(email, new_password)
            return redirect('login')  
        except ValueError as e:
            return render(request, 'reset_password.html', {'error': str(e)})

    return render(request, 'accounts/reset_password.html')


@login_required
def dashboard(request):
    # ดึงข้อมูลไฟล์ทั้งหมดที่ผู้ใช้งานนี้อัปโหลด
    user_files = MyFiles.objects.filter(user=request.user)  # ดึงข้อมูลไฟล์ที่เชื่อมโยงกับผู้ใช้งานนี้

    context = {
        'user_files': user_files,  # ส่งข้อมูลไฟล์ไปยัง template
    }

    return render(request, 'accounts/dashboard.html', context)
