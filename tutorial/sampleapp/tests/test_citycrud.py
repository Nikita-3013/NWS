from unittest import TestCase
from sampleapp.database.citiesCrud import *

class citiescrudTestCase(TestCase):
    def test_getCities(self):
        citylist = getCities()
        self.assertGreater(len(citylist) , 0)

    def test_getByCityName(self):
        obj = getByCityName('New York')
        self.assertNotEqual(obj.latitude ,0)
        self.assertNotEqual(obj.longitude,0)
    
    def test_invalid_getByCityName(self):
        obj = getByCityName('New Yor')
        self.assertEqual(obj.latitude ,0)
        self.assertEqual(obj.longitude,0)