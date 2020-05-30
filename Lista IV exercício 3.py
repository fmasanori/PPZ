from random import randint
v1 = []
v2 = []
v3 = []
for k in range(10):
  x = randint(1, 100)
  v1.append(x)
  v3.append(x)
  x = randint(1, 100)
  v2.append(x)
  v3.append(x)
print('v1:', v1)
print('v2:', v2)
print('v3:', v3)
