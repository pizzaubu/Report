# ในไฟล์ views.py
from django.shortcuts import render, redirect
from .forms import MeetingForm

def create_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # สามารถเปลี่ยนไปยังหน้าอื่นก็ได้
    else:
        form = MeetingForm()

    return render(request, 'meeting/create_meeting.html', {'form': form})
