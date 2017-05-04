from datetime import datetime, timedelta

from django.http import JsonResponse
from django.shortcuts import render

from secureporter.models import Records
from secureporter.plotdata import PlotData, PlotDataEncoder, PlotItem
from secureporter.util import dt_util


def RawDataView(request):
    return render(request, "rawdata.html", {
        'current_time': str(datetime.now()),
    })

def fail_rate(request):
    start = request.GET.get('start', None)
    end = request.GET.get('end', None)
    device = request.GET.get('device', None)

    datetime_start, datetime_end = dt_util.datetime_parse(start, end)
    fail_count, total_count, failurerate = Records.objects.fail_rate_by_time(device=device, \
                            start=datetime_start, end=datetime_end)

    return JsonResponse( \
            {"fail_rate" : failurerate, "fail_count": fail_count, \
             "total_count": total_count})

def plotdata(request):
    start = request.GET.get('start', None)
    end = request.GET.get('end', None)
    device = request.GET.get('device', None)

    datetime_start, datetime_end = dt_util.datetime_parse(start, end)
    raw2response = responseslot(device, datetime_start, datetime_end)
    return JsonResponse([raw2response], encoder=PlotDataEncoder, safe=False)

def responseslot(device, start, end):
    records = Records.objects.response_by_time(device=device, \
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

def delete_everything(request):
    Records.objects.all().delete()
    return JsonResponse({"result": "all records had been deleted."})
