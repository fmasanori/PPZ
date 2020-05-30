from random import sample
vetor = sample(range(100), 10)
maior = menor = vetor[0]
for x in vetor[1:]:
  if x > maior: maior = x
  if x < menor: menor = x
print ('Vetor:', vetor)
print (f'Maior: {maior}')
print (f'Menor: {menor}')



