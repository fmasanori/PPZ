from random import sample
vetor = sample(range(100), 20)
pares = []
ímpares = []
for x in vetor:
  if x % 2 == 0:
    pares.append(x)
  else:
    ímpares.append(x)
print ('Vetor', vetor)
print ('Pares', pares)
print ('Ímpares', ímpares)
