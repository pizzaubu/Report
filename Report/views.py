from django.shortcuts import render
from allfiles.models import MeetingReport


def home(request):
    reports = MeetingReport.objects.all().filter(is_available=True)
    print(reports)

    context = {
        'reports': reports,
        #'reports': [],
    }
    return render(request, 'home.html', context)