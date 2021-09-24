from unittest import TestCase
from sampleapp.views import *
from django.test.client import RequestFactory

class viewsTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_getforecast(self):
        # Create an instance of a GET request.
        request = self.factory.get('getforecast',{'cityName':'New York'})

        # Test my_view() as if it were deployed at /customer/details
        response = getforecast(request)
        self.assertEqual(response.status_code, 200)

