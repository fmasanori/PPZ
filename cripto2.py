arq = open('mensagem.txt', 'r')
sai = open('cripto.txt', 'w')
for linha in arq.readlines():
    saida = ''
    for c in linha:
        if c in 'aeiouãõ':
            saida += '*'
        else:
            saida += c
    sai.write(saida)
arq.close()
sai.close()
