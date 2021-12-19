import requests, json, re


response = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?limit=100&offset=0&datasetid=normal_dly&datatypeid=dly-tmin-normal&datatypeid=dly-tmax-normal&datatypeid=dly-tavg-normal&datatypeid=dly-prcp-normal&stationid=GHCND%3AUSC00020060&startdate=2010-02-01&enddate=2010-02-28T07%3A00%3A00.000', headers={'token': 'FqVETqfxQksyfJYSwEeGvMIeQiliHRct'})
data = json.loads(response.text)
#print (data["results"][0]["station"])



for result in data["results"]:
    data_date = result["date"]
    x = re.findall("\d{2}", data_date)
    data_dateyear = x[0] + x[1]
    data_datemonth = x[2]
    data_dateday = x[3]

    data_datatype = result["datatype"]
    #Three datatypes
    # DLY-TMAX-NORMAL
    # DLY-TMIN-NORMAL
    # DLY-TAVG-NORMAL

    data_station_raw = result["station"]
    #data_station_number = re.findall("GHCND:(.*)", data_station_raw) #get the actual station number

    data_value = float(result["value"]/10) #they store the float as a 3-digit integer in their API must convert to real float

    #print (data_station)
