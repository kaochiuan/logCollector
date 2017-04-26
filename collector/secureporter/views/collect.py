from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from secureporter.serializers import RecordSerializer
from secureporter.models import Records
from django.shortcuts import redirect
import json

class LogCollectViewSet(viewsets.ModelViewSet):
    queryset = Records.objects.all()
    serializer_class = RecordSerializer

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