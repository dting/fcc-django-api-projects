from django.conf.urls import url

from timestamp.views import parse_unix
from timestamp.views import parse_natural

urlpatterns = [
    url(r'^(?P<unix>[0-9]+)/$', parse_unix.as_view(), name='parse_unix'),
    url(r'^(?P<natural>.+)/$', parse_natural.as_view(), name='parse_natural')
]
