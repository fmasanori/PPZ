f = open('surf.txt')
primeiro = 0
segundo = 0
terceiro = 0
for linha in f:
    nome, pontos = linha.split()
    if float(pontos) > primeiro:
        terceiro = segundo
        segundo = primeiro
        primeiro = float(pontos)
    elif float(pontos) > segundo:
        terceiro = segundo
        segundo = float(pontos)
    elif float(pontos) > terceiro:
        terceiro = float(pontos)
f.close()

print(primeiro)
print(segundo)
print(terceiro)
        
