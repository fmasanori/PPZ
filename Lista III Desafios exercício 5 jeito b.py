n = int(input('Número: '))
inv = 0
while n > 0:
  inv *= 10
  inv += n % 10
  n //= 10
print(inv)
