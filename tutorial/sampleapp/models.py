from django.db import models
import json

# Create your models here.
class City():
    def __init__(self,name,latitude=0,longitude=0,temperature=0):
        self.name = name
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.temperature = float(temperature)


class GridPoint():
    def __init__(self,Id,GridX,GridY):
        self.Id = Id
        self.GridX = GridX
        self.GridY = GridY