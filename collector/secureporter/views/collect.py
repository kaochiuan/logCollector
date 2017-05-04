from datetime import datetime

from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from secureporter.models import Records
from secureporter.serializers import RecordSerializer


class LogCollectViewSet(viewsets.ModelViewSet):
    queryset = Records.objects.all()
    serializer_class = RecordSerializer

    def list(self, request):
        start = request.GET.get('start', None)
        end = request.GET.get('end', None)
        device = request.GET.get('device', None)
        if start is not None:
            datetime_start = datetime.strptime(start, '%Y-%m-%d')
        else:
            datetime_start = None
        if end is not None:
            datetime_end = datetime.strptime(end, '%Y-%m-%d')
        else:
            datetime_end = None

        if datetime_start is not None and datetime_end is not None:
            queryset = Records.objects.search_by_time(device, datetime_start, datetime_end)
        else:
            queryset = Records.objects.all()

        serializer = RecordSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        self.permission_classes = (AllowAny,)

        return super(LogCollectViewSet, self).get_permissions()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def favicon_redirect(request):
    return redirect('/static/secureporter/images/favicon.ico')
