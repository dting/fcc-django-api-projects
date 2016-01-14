from django.conf.urls import url

from url_shortener.views import shorten_url
from url_shortener.views import lengthen_url

urlpatterns = [
    url(r'^new/(?P<long_url>.+)/$', shorten_url.as_view(), name='shorten_url'),
    url(r'^(?P<short_url>.+)/$', lengthen_url.as_view(), name='lengthen_url')
]
