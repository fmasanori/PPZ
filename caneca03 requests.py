import requests
url = 'http://beans.itcarlow.ie/prices-loyalty.html'
texto = requests.get(url).text  
preço = texto[234:238]
print (preço)

