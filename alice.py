texto = open('alice.txt').read().lower()
from string import punctuation
for c in punctuation:
  texto = texto.replace(c, ' ')
texto = texto.split()
for p in texto:
  if p not in dic:
    dic[p] = 1
  else:
    dic[p] += 1
print (f'{dic["alice"]} vezes')

