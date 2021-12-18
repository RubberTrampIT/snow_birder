from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    #return HttpResponse("Hello, mars")
    import requests
    response = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?limit=100&offset=0&datasetid=normal_dly&datatypeid=dly-tmin-normal&datatypeid=dly-tmax-normal&datatypeid=dly-tavg-normal&datatypeid=dly-prcp-normal&stationid=GHCND%3AUSC00020060&startdate=2010-02-01&enddate=2010-02-28T07%3A00%3A00.000', headers={'token': 'FqVETqfxQksyfJYSwEeGvMIeQiliHRct'})
    return HttpResponse(response.text)
