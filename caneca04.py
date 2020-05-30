import urllib.request
pagina = urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html') 
texto = pagina.read().decode('utf8') 
onde = texto.find('>$')
inicio = onde + 2
fim = inicio + 4
preço = texto[inicio:fim]
print (preço)

