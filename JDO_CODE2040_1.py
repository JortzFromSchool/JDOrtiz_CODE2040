#J.D. Ortiz
#CODE2040 Stage 1
#Token = pDZFfWX5pw

#imports
import json, requests, re
from json import dumps, loads
from urllib2 import Request, urlopen

#request valuess
sendInfo = {'token' : 'pDZFfWX5pw'}
location = "http://challenge.code2040.org/api/getstring"

#create string
strResp = loads(urlopen(Request(location,data=json.dumps(sendInfo))).read())['result']

#reversal
revStr = strResp[::-1]

#post values
loc2 = "http://challenge.code2040.org/api/validatestring"
data2 = {'token' : 'pDZFfWX5pw', 'string': revStr }
validStr = requests.post(loc2, data=json.dumps(data2))