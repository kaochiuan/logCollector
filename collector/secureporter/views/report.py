from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from rest_pandas import PandasView
from secureporter.serializers import RecordSerializer
from secureporter.models import Records
from rest_framework.permissions import AllowAny
import pandas as pd
import json
# Create your views here.

class CollectReportView(PandasView):
    queryset = Records.objects.all()
    serializer_class = RecordSerializer

    def get_permissions(self):
        self.permission_classes = (AllowAny,)
        return super(CollectReportView, self).get_permissions()

def HelloWorldView(request):
    return render(request, "hello.html", {
        'current_time': str(datetime.now()),
    })

def ReportView(request):
    return render(request, "report.html", {
        'current_time': str(datetime.now()),
    })