from banco import *
from fatec import *

itens   = ["Esfiha", "Coxinha", "Pastel", "Pão de Queijo"] 
preços  = [1.50, 2.20, 1.80, 1.20] 
rodando = True 

while rodando: 
    opção = 1 
    for escolha in itens: 
        print(str(opção) + ". " + escolha) 
        opção = opção + 1 
    print(str(opção) + ". Finalizar") 
    escolha = int(input("Escolha uma opção: ")) 
    if escolha == opção:
        #escolheu a última opção Finalizar
        rodando = False 
    else: 
        cartão = input("Número do cartão de crédito: ")
        preço = desconto(preços[escolha - 1])
        salva_transação(preço, cartão, itens[escolha - 1])
        
