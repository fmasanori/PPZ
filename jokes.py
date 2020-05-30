import urllib.request
import json

url = 'http://api.icndb.com/jokes/random?limitTo=[nerdy]'

resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))

print (data['value']['joke'])

