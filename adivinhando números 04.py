from random import randint
print ('Bem vindo!')
sorteado = randint (1, 100)
chute = 0
while chute != sorteado:
    chute = int(input ('Chute um número: '))
    if chute == sorteado:
        print ('Você venceu!')
    else:
        if chute > sorteado:
            print ('Alto')
        else:
            print ('Baixo')
print ('Fim do jogo!')

