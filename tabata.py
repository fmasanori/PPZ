import requests
total = 0
for pag in range(1, 100):
  u = f'https://dadosabertos.camara.leg.br/api/v2/deputados/204534/despesas?ano=2020&ano=2019&pagina={pag}&itens=100'
  r = requests.get(u).json()
  for gasto in r['dados']:
    print (gasto['ano'], gasto['mes'], gasto['numDocumento'])
    total = total + float(gasto['valorLiquido'])

print (f'R$ {total:.2f}')
##
##import requests
##url = 'https://dadosabertos.camara.leg.br/api/v2/deputados/204534/despesas?ordem=ASC&ordenarPor=ano'
##resp = requests.get(url).json()
##total = 0
##for pag in range(1, 100):
##  u = f'https://dadosabertos.camara.leg.br/api/v2/deputados/204534/despesas?ordem=ASC&ordenarPor=ano&pagina={pag}&itens=100'
##  r = requests.get(u).json()
##  for gasto in r['dados']:
##    print (gasto['ano'], gasto['mes'], gasto['numDocumento'])
##    total = total + float(gasto['valorLiquido'])
##
##print (f'R$ {total:.2f}')
