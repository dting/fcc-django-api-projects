from django.views.generic import View
from django.http import JsonResponse
import re

class parse_header(View):
    def get(self, request):
        meta = request.META
        return JsonResponse({
            'ipaddress': meta.get('HTTP_X_FORWARDED_FOR') or meta.get('IP'),
            'language': meta['HTTP_ACCEPT_LANGUAGE'].split(",")[0],
            'software': re.search('\((.+?)\)', meta['HTTP_USER_AGENT']).group(1)
        })