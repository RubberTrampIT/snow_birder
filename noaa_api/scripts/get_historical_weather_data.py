import requests, json

response = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?limit=100&offset=0&datasetid=normal_dly&datatypeid=dly-tmin-normal&datatypeid=dly-tmax-normal&datatypeid=dly-tavg-normal&datatypeid=dly-prcp-normal&stationid=GHCND%3AUSC00020060&startdate=2010-02-01&enddate=2010-02-28T07%3A00%3A00.000', headers={'token': 'FqVETqfxQksyfJYSwEeGvMIeQiliHRct'})
data = json.loads(response.text)

print(data["results"][0])
