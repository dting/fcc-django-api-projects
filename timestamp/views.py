from django.views.generic import View
from django.http import JsonResponse

from datetime import datetime
from calendar import timegm

class parse_unix(View):
    err_res = {'unix': None, 'natural': None}
    def get(self, request, unix):
        res = {}
        try:
            utc_dt = datetime.utcfromtimestamp(float(unix))
            res['unix'] = int(unix)
            res['natural'] = utc_dt.strftime("%B %d, %Y")
        except ValueError:
            res = self.err_res;
        return JsonResponse(res)
        
class parse_natural(View):
    err_res = {'unix': None, 'natural': None}
    def get(self, request, natural):
        res = {}
        try:
            d = datetime.strptime(natural, "%B %d, %Y")
            res['unix'] = int(timegm(d.timetuple()))
            res['natural'] = natural
        except ValueError:
            res = self.err_res;
        return JsonResponse(res)