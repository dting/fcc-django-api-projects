from django.views.generic import View
from django.http import JsonResponse
from django.core import serializers

from image_search.models import Search

import os
import urllib, urllib2
import json

base_url = 'https://www.googleapis.com/customsearch/v1' 
search_url = (base_url + '?searchType=image&key={}&cx={}&q=').format(
    os.environ.get('GOOGLE_API_KEY'), 
    os.environ.get('GOOGLE_CX')
)

class search(View):
    def get(self, request, terms):
        url = search_url + urllib.quote(terms, safe="%/:=&?~#+!$,;'@()*[]")
        start = request.GET.get('offset')
        if start and start.isdigit():
            url += '&start={}'.format(start)
        
        response = urllib2.urlopen(url, None, 2000)
        if response.getcode() != 200:
            return JsonResponse({'error': response.getcode()})
        data = json.load(response)
        res = []
        for item in data['items']:
            res.append({
                'url': item['link'],
                'snippet': item['snippet'],
                'thumbnail': item['image']['thumbnailLink'],
                'context': item['image']['contextLink']
            })
            
        Search.objects.create(terms=terms)
        return JsonResponse(res, safe=False)
        
class latest(View):
    def get(self, request):
        searches = Search.objects.all().order_by('-id')[:10]
        data = json.loads(serializers.serialize('json', searches))
        return JsonResponse(data, safe=False)