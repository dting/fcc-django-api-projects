from django.test import TestCase
from django.test import Client

from django.core.urlresolvers import reverse

class TimestampTest(TestCase):
        
    def test_unix_timestamp_req_returns_epoch_and_natural_result(self):
        client = Client()
        response = client.get(reverse('parse_unix', args=[0]))
        
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {
                'unix': 0,
                'natural': 'January 01, 1970'
            }
        )
        
    def test_natural_req_returns_epoch_and_natural_result(self):
        d_str = 'December 15, 2015'
        client = Client()
        response = client.get(reverse('parse_natural', args=[d_str]))
        
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {
                'unix': 1450137600,
                'natural': d_str
            }
        )
        
    def test_invalid_date_string_return_null_values(self):
        d_str = 'asdf'
        client = Client()
        response = client.get(reverse('parse_natural', args=[d_str]))
        
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {
                'unix': None,
                'natural': None
            }
        )