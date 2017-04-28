from django.shortcuts import render
from datetime import datetime
from secureporter.models import Records
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.

def RawDataView(request):
    return render(request, "rawdata.html", {
        'current_time': str(datetime.now()),
    })

def fail_rate(request):
    start = request.GET['start']
    end = request.GET['end']

    datetime_start = datetime.strptime(start, '%Y-%m-%d')
    datetime_end = datetime.strptime(end, '%Y-%m-%d')
    failurerate = Records.objects.fail_rate_by_time(datetime_start, datetime_end)

    return JsonResponse({"failure_rate" : failurerate})
