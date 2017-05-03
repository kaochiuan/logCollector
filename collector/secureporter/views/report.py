from django.shortcuts import render
from datetime import datetime
from secureporter.models import Records
from rest_framework.response import Response
from django.http import JsonResponse
from datetime import timedelta
from math import ceil
from secureporter.plotdata import PlotItem, PlotData, PlotDataEncoder, PlotItemEncoder
import json

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
    failurerate = Records.objects.fail_rate_by_time(device=None, \
                            start=datetime_start, end=datetime_end)

    return JsonResponse({"failure_rate" : failurerate})

def plotdata(request):
    start = request.GET['start']
    end = request.GET['end']
    datetime_start = datetime.strptime(start, '%Y-%m-%d')
    datetime_end = datetime.strptime(end, '%Y-%m-%d')
    #raw2failrate = failrateslot(datetime_start, datetime_end)
    raw2response = responseslot(datetime_start, datetime_end)
    #dumps = json.dumps(raw2result, cls=PlotDataEncoder)
    return JsonResponse([raw2response], encoder=PlotDataEncoder, safe=False)

def failrateslot(start, end):
    interval = end - start
    slot_interval = interval.total_seconds() / timedelta(minutes=5).total_seconds()
    slot = ceil(slot_interval)

    slot_list = []
    for index in range(0, slot):
        slot_date_start = start + timedelta(minutes=5) * index
        slot_date_end = slot_date_start + timedelta(minutes=5)
        failrate = Records.objects.fail_rate_by_time(device=None, \
                                    start=slot_date_start, end=slot_date_end)
        item = PlotItem(date=slot_date_start, value=failrate)
        slot_list.append(item)

    plot_data = PlotData(id="fail rate", label="Fail rate", unit="%", itemlist=slot_list)
    return plot_data

def responseslot(start, end):
    interval = end - start
    slot_interval = interval.total_seconds() / timedelta(minutes=5).total_seconds()
    slot = ceil(slot_interval)

    records = Records.objects.response_by_time(device=None, \
                                    start=start, end=end)
    slot_list = []
    for rec in records:
        if rec.spent_seconds is None:
            response_time = 0
        else:
            response_time = rec.spent_seconds

        item = PlotItem(date=rec.record_dt, value=response_time)
        slot_list.append(item)

    plot_data = PlotData(id="response time", label="Response time", unit="seconds", \
                itemlist=slot_list)
    return plot_data
