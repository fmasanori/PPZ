print ('Bem vindo!')
chute = 0
while chute != 42:
    g = input ('Chute um número: ')
    chute = int(g)
    if chute == 42:
        print ('Você venceu!')
    else:
        if chute > 42:
            print ('Alto')
        else:
            print ('Baixo')
print ('Fim do jogo!')

