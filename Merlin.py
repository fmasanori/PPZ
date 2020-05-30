def enumerações(items):
    n = len(items)
    s = [0]*(n+1)
    k = 0
    while True:
        if s[k] < n:
            s[k+1] = s[k] + 1
            k += 1
        else:
            s[k-1] += 1
            k -= 1
        if k == 0:
            break
        else:
            lista = []
            for j in range(1, k+1):
                lista.append(items[s[j]-1])
            yield lista

def combinações(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in combinações(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def permutações(items):
    return combinações(items, len(items))

#troque o código abaixo pela sua implementação
#faça a leitura de casamento.txt e cavaleiros.txt
#e monte os dicionários de amados e amigos
#depois implemente sua lógica para dizer se é possível
#o casamento e sentar na mesa sem brigar, não é necessário
#mostrar o casamento concreto possível
print ('Permutações')
for p in permutações(['Adriano','Bruno', 'Diogo', 'Eclis', 'Gabriel', 'Leandro', 'Walber']):
    print (p)

print ('Enumerações')
for p in enumerações(['Jessica', 'Fernanda', 'Pamela', 'Renata']):
    print (p)
