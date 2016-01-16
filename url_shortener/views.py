from django.views.generic import View
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

from url_shortener.models import ShortUrl
from math import pow

CHAR_MAP = 'rVLHs5NTGyz9KWq0ndtlZBcMXQkp4187CgFfbJvh2RxmSj6P3wYD'
BASE = len(CHAR_MAP)

class shorten_url(View):
    def get(self, request, long_url):
        url_validator = URLValidator()
        try:
            url_validator(long_url)
        except ValidationError as e:
            print("shorten_url error: {}".format(e))
            return JsonResponse({'error': 'URL invalid'})
        s = ShortUrl.objects.create(long_url=long_url)
        short_url = reverse('lengthen_url', args=[self.id_to_short_url(s.id)])
        return JsonResponse({
            'original_url': long_url,
            'short_url': request.build_absolute_uri(short_url)
        })
        
    def id_to_short_url(self, n):
        surl = ''
        while n:
            surl += CHAR_MAP[n % BASE]
            n //= BASE
        return surl        
        
class lengthen_url(View):
    def get(self, request, short_url):
        try:
            s = ShortUrl.objects.get(pk=self.short_url_to_id(short_url))
        except (ValueError, ShortUrl.DoesNotExist) as e:
            print("lengthen_url error: {}".format(e))
            return JsonResponse({'error': 'No short url found for given input'})
        return redirect(s.long_url)
        
    def short_url_to_id(self, surl):
        return sum(CHAR_MAP.index(c) * int(pow(BASE, idx)) for idx, c in enumerate(surl))