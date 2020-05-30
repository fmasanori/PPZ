minutos = int(input('Minutos: '))
if minutos < 200:
  preço = 0.2
elif minutos <= 400:
  preço = 0.18
elif minutos <= 800:
  preço = 0.15
else:
  preço = 0.08
print (f'R$ {preço*minutos:.2f}')


