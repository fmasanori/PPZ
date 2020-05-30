n = int(input('N: '))
k = 1
while k * (k + 1) * (k + 2) < n:
    k = k + 1

print (k * (k + 1) * (k + 2) == n)
