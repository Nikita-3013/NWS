from django.db import connection
from sampleapp.models import *

def getCities():
    cursor = connection.cursor()
    cityList=[]
    try:
        cursor.execute("SELECT City,Lat,Long FROM cities")
        
        result_set = cursor.fetchall()
        for row in result_set:
            cityList.append(City(row[0]))
    finally:
        cursor.close()
    return cityList

def getByCityName(cityName):
    cursor = connection.cursor()
    CityObj=City(cityName)
    try:
        cursor.execute("SELECT City,Lat,Long FROM cities WHERE City=%s",[cityName])
        
        result_set = cursor.fetchall()
        
        for row in result_set:
            CityObj=City(cityName,row[1],row[2])

    finally:
        cursor.close()
    return CityObj

