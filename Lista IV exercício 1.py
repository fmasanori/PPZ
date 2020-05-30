from random import sample
vetor = sample(range(100), 10)
maior = menor = vetor[0]
k = 1
while k < 10:
  if vetor[k] > maior: maior = vetor[k]
  if vetor[k] < menor: menor = vetor[k]
  k = k + 1
print ('Vetor:', vetor)
print (f'Maior: {maior}')
print (f'Menor: {menor}')

