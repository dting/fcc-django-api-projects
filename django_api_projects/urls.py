"""django_api_projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from timestamp_microservice.views import parse_unix
from timestamp_microservice.views import parse_natural

urlpatterns = [
    url(r'^api/timestamp-microservice/(?P<unix>[0-9]+)/$', parse_unix.as_view(), name='parse_unix'),
    url(r'^api/timestamp-microservice/(?P<natural>.+)/$', parse_natural.as_view(), name='parse_natural'),
    url(r'^admin/', admin.site.urls),
]
