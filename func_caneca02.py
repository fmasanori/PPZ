import urllib.request
import time
def pega_preço():
    pagina = urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html') 
    texto = pagina.read().decode('utf8') 
    onde = texto.find('>$')
    inicio = onde + 2
    fim = inicio + 4
    return float(texto[inicio:fim])

opção = input('Deseja comprar já? (S/N)').upper()
if opção == 'S':
    preço = pega_preço()
    print (f'Comprar! R$ {preço:.2f}')  
else:
    preço = 99.99
    while preço >= 4.74:
        preço = pega_preço()
        if preço >= 4.74:
            time.sleep(600) 
    print (f'Comprar! R$ {preço:.2f}')  

