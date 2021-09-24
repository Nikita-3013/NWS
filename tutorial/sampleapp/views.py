from django.shortcuts import render
from django.http import HttpResponse
from sampleapp.models import City
from sampleapp.database.citiesCrud import *
from sampleapp.NWSProvider.NWSDataProvider import *
import json
# Create your views here.
def welcome(request):
    return render(request, 'website/welcome.html',{'cities': getCities()})

def getforecast(request):
    jsondata = {}
    try:
        cityName = request.GET.get('cityName').strip()
        # get city object db by city name
        Cityobj = getByCityName(cityName)
        
        data = getforecastByCity(Cityobj)
        tempObj ={'cityName':data.name,'lat':data.latitude,'long':data.longitude,'temp':data.temperature} 
        
        
        jsondata = json.dumps(tempObj)
    except:
        print("error")

    return HttpResponse(jsondata, content_type='application/json')

