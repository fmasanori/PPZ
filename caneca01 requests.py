import requests
url = 'http://beans.itcarlow.ie/prices.html'
texto = requests.get(url).text
print (texto)

