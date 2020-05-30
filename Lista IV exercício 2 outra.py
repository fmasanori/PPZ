from random import sample
vetor = sample(range(100), 20)
par = [x for x in vetor if x % 2 == 0]
ímpar = [x for x in vetor if x % 2 == 1]
print ('Vetor', vetor)
print ('Pares', par)
print ('Ímpares', ímpar)
