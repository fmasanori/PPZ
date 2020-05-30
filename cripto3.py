texto = open('mensagem.txt')
cripto = open('cripto.txt', 'w')

for caracter in texto.read():
  if caracter in 'aeiouãõáéíóú':
    cripto.write('*')
  else:
    cripto.write(caracter)

texto.close()
cripto.close()

