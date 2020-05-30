def salva_transação(preço, cartão_crédito, descrição):
    file = open("transações.txt", "a")
    file.write("%07d%16s%16s\n"
               %(preço * 100, cartão_crédito, descrição))
    file.close()
