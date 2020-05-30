peso = float(input('Peso: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    multa = excesso = 0

print (f'Multa de R$ {multa:.2f}')
print (f'Excesso: {excesso:.2f}')
