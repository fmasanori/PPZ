f = open('surf.txt')
notas = []
for linha in f:
    nome, pontos = linha.split()
    notas.append(float(pontos))
f.close()
notas.sort()

print (notas[:3])

