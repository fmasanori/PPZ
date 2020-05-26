from random import randint
secreta = randint(1, 100)
while True:
  chute = int(input('Chute: '))
  if chute == secreta:
    print (f'Acertou o número {secreta}')
    break
  else:
    print ('Alto' if chute > secreta else 'Baixo')
print ('Fim de jogo')
