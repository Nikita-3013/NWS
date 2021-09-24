import requests
from sampleapp.models import *

def getforecastByCity(cityobj):
    try:
        gridpoint = getGridPoint(cityobj.latitude,cityobj.longitude)
        url='https://api.weather.gov/gridpoints/'+ str(gridpoint.Id)+'/'+str(gridpoint.GridX)+','+ str(gridpoint.GridY)+'/forecast'
        response = requests.get(url)
        jsondata = response.json()
        temp = jsondata['properties']['periods'][0]['temperature']
        city = City(cityobj.name,cityobj.latitude,cityobj.longitude,temp)
        return city
    except:
        return None


def getGridPoint(lat,lng):
    try:
        url='https://api.weather.gov/points/'+ str(lat) +','+ str(lng)
        response = requests.get(url)
        jsondata = response.json()
        gridpoint = GridPoint(jsondata['properties']['gridId'],jsondata['properties']['gridX'],jsondata['properties']['gridY'])
        return gridpoint
    except:
        return None
    