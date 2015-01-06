#J.D. Ortiz
#CODE2040 Stage 1
#Token = pDZFfWX5pw

#imports
import json, requests, re
from json import dumps, loads
from urllib2 import Request, urlopen

#request values
sendInfo = {'token' : 'pDZFfWX5pw'}
location = "http://challenge.code2040.org/api/haystack"

#get string dictionary
stringDict = loads(urlopen(Request(location,data=json.dumps(sendInfo))).read())['result']

#search for needle
needle = stringDict['needle']
haystack = stringDict['haystack']
index = -1 #if not found result will be negative

#loop
for hay in range(len(haystack)):
	if (haystack[hay] == needle):
		index = hay

#post values
loc2 = "http://challenge.code2040.org/api/validateneedle"
data2 = {'token' : 'pDZFfWX5pw', 'needle': index}
valid = requests.post(loc2, data=json.dumps(data2))
print(valid.content)