#J.D. Ortiz
#CODE2040 Stage 3
#Token = pDZFfWX5pw

#imports
import json, requests, re
from json import dumps, loads
from urllib2 import Request, urlopen

#request values
sendInfo = {'token' : 'pDZFfWX5pw'}
location = "http://challenge.code2040.org/api/prefix"

#get string dictionary
prefixArray= loads(urlopen(Request(location,data=json.dumps(sendInfo))).read())['result']

#search for needle
prefix = prefixArray['prefix']
array = prefixArray['array']
exclusiveArray = []

#loop
for word in range(len(array)):
	if not(array[word].startswith(prefix)):
		exclusiveArray.append(array[word])

#post values
loc2 = "http://challenge.code2040.org/api/validateprefix"
data2 = {'token' : 'pDZFfWX5pw', 'array': exclusiveArray}
valid = requests.post(loc2, data=json.dumps(data2))
print(valid.content)