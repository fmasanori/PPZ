m = float(input('Preço: '))
p = float(input('Desconto%: '))
desconto = m * p / 100
novo = m - desconto
print(f'Desconto: R$ {desconto:.2f}')
print(f'Preço a pagar: {novo:.2f}')
