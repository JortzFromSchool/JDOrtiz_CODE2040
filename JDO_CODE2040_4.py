#J.D. Ortiz
#CODE2040 Stage 4
#Token = pDZFfWX5pw

#imports
import json, requests, re, datetime
from datetime import timedelta
from json import dumps, loads
from urllib2 import Request, urlopen

#request values
sendInfo = {'token' : 'pDZFfWX5pw'}
location = "http://challenge.code2040.org/api/time"

#get time dictionary
timeDict= loads(urlopen(Request(location,data=json.dumps(sendInfo))).read())['result']

#because we imported the python datetime library, the following works:
datestamp = timeDict['datestamp']
interval = timeDict['interval']

#butcher the datestamp: standardize irregular characters
datestamp = datestamp.replace("T",".")
datestamp = datestamp.replace(":",".")
datestamp = datestamp.replace('-',".")
datestamp = datestamp.replace("Z","")
#split along irregulars
strVals = datestamp.split(".")

#conversion to ints
intVals = []
for num in strVals:
	intVals.append(int(num))

#conversion to datetime class
date = datetime.datetime(intVals[0],intVals[1],intVals[2],intVals[3],intVals[4],intVals[5],intVals[6])

#addition of interval, cast to string
datestamp2 = str(date + timedelta(seconds=interval))


#post values
loc2 = "http://challenge.code2040.org/api/validatetime"
data2 = {'token' : 'pDZFfWX5pw', 'datestamp': datestamp2 }
valid = requests.post(loc2, data=json.dumps(data2))
print(valid.content)