from django.conf.urls import url, include
from django.contrib import admin

from req_header_parser.views import parse_header
from file_metadata.views import upload_file
from home.views import home

urlpatterns = [
    url(r'^api/timestamp/', include('timestamp.urls')),
    url(r'^api/request-header-parser/$', parse_header.as_view(), name='parse_header'),
    url(r'^api/url-shortener/', include('url_shortener.urls')),
    url(r'^api/image-search/', include('image_search.urls')),
    url(r'^api/file-metadata/$', upload_file, name='upload_file'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home.as_view(), name='home')
]
