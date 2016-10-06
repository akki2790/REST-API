#python code to request a web page
from urllib2 import Request, urlopen, URLError

request = Request('https://motorcycles.com/')

try:
    response = urlopen(request)
    motorcycles=response.read()
    print motorcycles[900:900]
except URLError, e:
    print 'No motorcycle. Got an error code' + e
