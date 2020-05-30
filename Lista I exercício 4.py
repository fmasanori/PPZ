s = float(input('Salário: '))
p = float(input('Aumento%: '))
aumento = s * p / 100
novo = s + aumento
print(f'Aumento: R$ {aumento:.2f}')
print(f'Novo salário: R$ {novo:.2f}')
