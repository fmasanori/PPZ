v = int(input('Velocidade: '))
if v > 110:
  print ('Você foi multado!')
  multa = (v - 110) * 5
  print (f'Multa R$ {multa:.2f}')
else:
  print ('Siga em frente')
