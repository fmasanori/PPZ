valor = float(input('Valor por hora: '))
horas = int(input('Horas tralhadas: '))
bruto = valor * horas
ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
liquido = bruto - ir - inss - sind
print (f'+Salário Bruto:\t\t R$ {bruto:.2f}')
print (f'-IR:\t\t\t R$ {ir:.2f}')
print (f'-INSS:\t\t\t R$ {inss:.2f}')
print (f'-Sindicato:\t\t R$ {sind:.2f}')
print (f'=Salário Líquido:\t R$ {liquido:.2f}')

