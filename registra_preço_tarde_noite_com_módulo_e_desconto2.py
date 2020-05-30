from banco import *
import fatec
import japa

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
        preço = fatec.desconto(preços[escolha - 1])
        if itens[escolha - 1] == 'Pastel':
            preço = japa.desconto(preço)
        salva_transação(preço, cartão, itens[escolha - 1])
        
