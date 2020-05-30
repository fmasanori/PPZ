import requests
url = 'http://api.icndb.com/jokes/random?limitTo=[nerdy]'
data = requests.get(url).json()
print (data['value']['joke'])

