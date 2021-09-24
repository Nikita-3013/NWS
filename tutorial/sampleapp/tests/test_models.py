from unittest import TestCase
from sampleapp.models import City,GridPoint

class testmodelsTestCase(TestCase):
    def test_grid(self):
        obj = GridPoint('12',1234,123)
        self.assertEqual(obj.Id,'12')
        self.assertEqual(obj.GridX,1234)
        self.assertEqual(obj.GridY,123)

    def test_city(self):
        obj = City('New York',40.1234,72.124)
        self.assertEqual(obj.name,'New York')
        self.assertEqual(obj.latitude,40.1234)
        self.assertEqual(obj.longitude,72.124)
