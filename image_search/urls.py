from django.conf.urls import url

from image_search.views import search
from image_search.views import latest

urlpatterns = [
    url(r'^search/(?P<terms>.+)/$', search.as_view(), name='search'),
    url(r'^latest/$', latest.as_view(), name='latest')
]
