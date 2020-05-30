a = int(input('Valor de a: '))
b = int(input('Valor de b: '))
while a % b != 0:
    a, b = b, a%b
print (f'mdc = {b}')
