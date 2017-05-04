"""collector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from secureporter.views import LogCollectViewSet, favicon_redirect, RawDataView, fail_rate, plotdata, delete_everything

router = routers.DefaultRouter()
router.register(r'records', LogCollectViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rawdata/$', RawDataView, name='raw log view'),
    url(r'^favicon.ico/$', favicon_redirect, name='favicon'),
    url(r'^failure_rate/$', fail_rate, name='failure_rate view'),
    url(r'^plotdata$', plotdata, name="plotdata"),
    url(r'^delete_everything$', delete_everything, name="delete_everything"),
]
