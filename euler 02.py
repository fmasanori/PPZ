def fib():
  a, b = 1, 1
  while True:
    yield b
    a, b = b, a + b

def pares(seq):
  for n in seq:
    if n % 2 == 0:
      yield n

def menores_4M(seq):
  for n in seq:
    if n > 4000000:
      break
    yield n   

print (sum(pares(menores_4M(fib()))))
    
