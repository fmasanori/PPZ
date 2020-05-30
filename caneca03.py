import urllib.request
pagina = urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html') 
texto = pagina.read().decode('utf8') 
preço = texto[234:238]
print (preço)

