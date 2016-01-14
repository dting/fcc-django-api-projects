from django.test import TestCase
from django.test import Client
import json

from django.core.urlresolvers import reverse

class RequestHeaderParserMicroserviceTest(TestCase):
        
    def test_request_header_parser(self):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
        x_forwarded_for = '1.2.3.4'
        ip = '2.3.4.5'
        accept_language = 'en-US,en;q=0.8'
        client = Client(
            HTTP_X_FORWARDED_FOR=x_forwarded_for,
            IP=ip,
            HTTP_USER_AGENT=user_agent, 
            HTTP_ACCEPT_LANGUAGE=accept_language
        )
        response = client.get(reverse('parse_header'))
        obj = json.loads(response.content)
        
        self.assertEqual(response.status_code, 200)
        self.assertEquals(obj['ipaddress'], x_forwarded_for)
        self.assertEquals(obj['language'], 'en-US')
        self.assertEquals(obj['software'], 'Macintosh; Intel Mac OS X 10_11_1')