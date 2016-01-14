from django.test import TestCase
from django.test import Client

from django.core.urlresolvers import reverse

from url_shortener.views import shorten_url, lengthen_url

class UrlShortenerTest(TestCase):
        
    def test_id_to_short_url_is_reversable(self):
        id = 323123
        s_view = shorten_url()
        l_view = lengthen_url()
        short_url = s_view.id_to_short_url(id)
        self.assertEquals(l_view.short_url_to_id(short_url), id)
        