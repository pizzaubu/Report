from django.shortcuts import render, redirect
from .forms import MeetingReportForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import MeetingReport

def create_report(request):
    if request.method == 'POST':
        form = MeetingReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = MeetingReportForm()

    return render(request, 'allfiles/create_report.html', {'form': form})

def edit_report(request, report_id):
    report = get_object_or_404(MeetingReport, pk=report_id)
    if request.method == 'POST':
        form = MeetingReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            # ลบไฟล์เก่าถ้ามีการอัปโหลดไฟล์ใหม่
            if 'file' in request.FILES:
                if report.file:
                    report.file.delete()
            form.save()
            return redirect('edit_report', report_id=report.id)
    else:
        form = MeetingReportForm(instance=report)
    return render(request, 'allfiles/edit_report.html', {'form': form, 'report': report})

def view_reports(request):
    reports = MeetingReport.objects.all()
    return render(request, 'allfiles/view_reports.html', {'reports': reports})