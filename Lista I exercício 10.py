'''
Fazendo uma regra de três
1 dia = 1440 minutos = 144 cigarros
'''
cigarros = int(input('Cigarros dia: '))
anos = int(input('Anos fumados: '))
total_cigarros = anos * 365 * cigarros
dias = total_cigarros / 144
print (f'Você perdeu {dias:.1f} dias')
