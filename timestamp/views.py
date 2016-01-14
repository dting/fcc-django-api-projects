from django.views.generic import View
from django.http import JsonResponse

from datetime import datetime
from calendar import timegm

err_res = {'unix': None, 'natural': None}

class parse_unix(View):
    def get(self, request, unix):
        res = {}
        try:
            utc_dt = datetime.utcfromtimestamp(float(unix))
            res['unix'] = int(unix)
            res['natural'] = utc_dt.strftime("%B %d, %Y")
        except ValueError:
            res = err_res;
        return JsonResponse(res)
        
class parse_natural(View):
    def get(self, request, natural):
        res = {}
        try:
            d = datetime.strptime(natural, "%B %d, %Y")
            res['unix'] = int(timegm(d.timetuple()))
            res['natural'] = natural
        except ValueError:
            res = err_res;
        return JsonResponse(res)