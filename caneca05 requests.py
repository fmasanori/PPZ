import requests
url = 'http://beans.itcarlow.ie/prices-loyalty.html'
texto = requests.get(url).text  
onde = texto.find('>$')
inicio = onde + 2
fim = inicio + 4
preço = texto[inicio:fim]
if preço < 4.74:
    print (preço)

