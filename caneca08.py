import urllib.request
import time
preço = 99.99
while preço >= 4.74:
    pagina = urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html') 
    texto = pagina.read().decode('utf8') 
    onde = texto.find('>$')
    inicio = onde + 2
    fim = inicio + 4
    preço = float(texto[inicio:fim])
    if preço >= 4.74:
        time.sleep(600) 
print (f'Comprar! R$ {preço:.2f}')

