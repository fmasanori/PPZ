f = open('surf.txt')
maior = 0
for linha in f:
    nome, pontos = linha.split()
    if float(pontos) > maior:
        maior = float(pontos)
f.close()
print (maior)
