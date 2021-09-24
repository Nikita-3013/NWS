from unittest import TestCase
from sampleapp.NWSProvider.NWSDataProvider import *
from sampleapp.models import City

class NWSDataProviderTestCase(TestCase):
    def test_get_valid_gridpoint(self):
        gridpoint = getGridPoint(40.6943,-73.9249)
        self.assertEqual(gridpoint.Id,'OKX')
    
    def test_get_invalid_gridpoint(self):
        gridpoint = getGridPoint(40.6943,40.6943)
        self.assertIsNone(gridpoint)

    def test_get_forecast(self):
        cityobj = City('New York',40.6943,-73.9249)
        resultcity = getforecastByCity(cityobj)
        self.assertIsInstance(resultcity,City)
        self.assertIsNotNone(resultcity.temperature)

    def test_get_invalidObj_forecast(self):
        cityobj = City('New York',40.6943,40.6943)
        resultcity = getforecastByCity(cityobj)
        self.assertIsNone(resultcity)
        