from django.shortcuts import render
from datetime import datetime
# Create your views here.

def HelloWorldView(request):
    return render(request, "hello.html", {
        'current_time': str(datetime.now()),
    })

def ReportView(request):
    return render(request, "report.html", {
        'current_time': str(datetime.now()),
    })

def RawDataView(request):
    return render(request, "rawdata.html", {
        'current_time': str(datetime.now()),
    })