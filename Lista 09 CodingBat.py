#!/usr/bin/python -tt
# Exercícios by Nick Parlante (CodingBat)

# A. first_last6
# verifica se 6 é o primeiro ou último elemento da lista nums
# first_last6([1, 2, 6]) -> True
# first_last6([6, 1, 2, 3]) -> True
# first_last6([3, 2, 1]) -> False
def first_last6(nums): #
  return

# B. same_first_last #
# retorna True se a lista nums possui pelo menos um elemento
# e o primeiro elemento é igual ao último
# same_first_last([1, 2, 3]) -> False
# same_first_last([1, 2, 3, 1]) -> True
# same_first_last([1, 2, 1]) -> True
def same_first_last(nums):
  return 

# C. common_end #
# Dada duas listas a e b verifica se os dois primeiros são
# iguais ou os dois últimos são iguais
# suponha que as listas tenham pelo menos um elemento
# common_end([1, 2, 3], [7, 3]) -> True
# common_end([1, 2, 3], [7, 3, 2]) -> False
# common_end([1, 2, 3], [1, 3]) -> True
def common_end(a, b):
  return 

# D. maior_ponta #
# Dada uma lista não vazia, cria uma nova lista onde todos
# os elementos são o maior das duas pontas
# obs.: não é o maior de todos, mas entre as duas pontas
# maior_ponta([1, 2, 3]) -> [3, 3, 3]
# maior_ponta([1, 3, 2]) -> [2, 2, 2]
def maior_ponta(nums):
  return

# E. sum2 #
# Dada uma lista de inteiros de qualquer tamanho
# retorna a soma dos dois primeiros elementos
# se a lista tiver menos de dois elementos, soma o que for possível
def sum2(nums):
  return 

# F. middle_way #
# sejam duas listas de inteiros a e b
# retorna uma lista de tamanho 2 contendo os elementos do
# meio de a e b, suponha que as listas tem tamanho ímpar
# middle_way([1, 2, 3], [4, 5, 6]) -> [2, 5]
# middle_way([7, 7, 7], [3, 8, 0]) -> [7, 8]
# middle_way([5, 2, 9], [1, 4, 5]) -> [2, 4]
def middle_way(a, b):
  return 

# G. date_fashion
# você e sua namorada(o) vão a um restaurante
# eu e par são as notas das suas roupas de 0 a 10
# quanto maior a nota mais chique vocês estão vestidos
# o resultado é se vocês conseguiram uma mesa no restaurante:
# 0=não 1=talvez e 2=sim
# se a nota da roupa de um dos dois for menor ou igual a 2
# vocês não terão direito à uma mesa (0)
# se as notas são maiores, então caso um dos dois esteja
# bem chique (nota >= 8) então a resposta é sim (2)
# caso contrário a resposta é talvez (1)
# date_fashion(5, 10) -> 2
# date_fashion(5, 2) -> 0
# date_fashion(5, 5) -> 1
def date_fashion(eu, par):
  return

# H. squirrel_play
# os esquilos na FATEC brincam quando a temperatura está entre 60 e 90
# graus Fahreneit (são estrangeiros e o termômetro é diferente rs)
# caso seja verão, então a temperatura superior é 100 no lugar de 90
# retorne True caso os esquilos brinquem
# squirrel_play(70, False) -> True
# squirrel_play(95, False) -> False
# squirrel_play(95, True) -> True
def squirrel_play(temp, is_summer):
  return

# I. pego_correndo
# você foi pego correndo
# o resultado será:
# sem multa = 0
# multa média = 1
# multa grave = 2
# velocide <= 60 sem multa
# velocidade entre 61 e 80 multa média
# velocidade maior que 81 multa grave (cidade do interior)
# caso seja seu aniversário a velocidade pode ser 5 km/h maior em todos os casos
# pego_correndo(60, False) -> 0
# pego_correndo(65, False) -> 1
# pego_correndo(65, True) -> 0 
def pego_correndo(speed, is_birthday):
  return

# J. alarm_clock #
# day: 0=domingo, 1=segunda, 2=terça, ..., 6=sábado
# vacation = True caso você esteja de férias
# o retorno é uma string que diz quando o despertador tocará
# dias da semana '07:00'
# finais de semana '10:00'
# a menos que você esteja de férias, neste caso:
# dias da semana '10:00'
# finais de semana 'off'
# alarm_clock(1, False) -> '7:00'
# alarm_clock(5, False) -> '7:00'
# alarm_clock(0, False) -> '10:00'
def alarm_clock(day, vacation):
  return

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('First_last6')
  test(first_last6([1, 2, 6]), True)
  test(first_last6([6, 1, 2, 3]), True)
  test(first_last6([3, 2, 1]), False)
  test(first_last6([3, 6, 1]), False)
  test(first_last6([3, 6]), True)
  test(first_last6([6]), True)
  test(first_last6([3]), False)

  print ()
  print ('Same_first_last')
  test(same_first_last([1, 2, 3]), False)
  test(same_first_last([1, 2, 3, 1]), True)
  test(same_first_last([1, 2, 1]), True)
  test(same_first_last([7]), True)
  test(same_first_last([]), False)
  test(same_first_last([7, 7]), True)

  print ()
  print ('Common_end')
  test(common_end([1, 2, 3], [7, 3]), True)
  test(common_end([1, 2, 3], [7, 3, 2]), False)
  test(common_end([1, 2, 3], [1, 3]), True)
  test(common_end([1, 2, 3], [1]), True)
  test(common_end([1, 2, 3], [2]), False)

  print ()
  print ('Maior_ponta')
  test(maior_ponta([1, 2, 3]), [3, 3, 3])
  test(maior_ponta([11, 5, 9]), [11, 11, 11])
  test(maior_ponta([2, 11, 3]), [3, 3, 3])
  test(maior_ponta([11, 3, 3]), [11, 11, 11])
  test(maior_ponta([3, 11, 11]), [11, 11, 11])
  test(maior_ponta([2, 2, 2]), [2, 2, 2])
  test(maior_ponta([2, 11, 2]), [2, 2, 2])
  test(maior_ponta([0, 0, 1]), [1, 1, 1])
  
  print ()
  print ('sum2')
  test(sum2([1, 2, 3]), 3)
  test(sum2([1, 1]), 2)
  test(sum2([1, 1, 1, 1]), 2)
  test(sum2([1, 2]), 3)
  test(sum2([1]), 1)
  test(sum2([]), 0)
  test(sum2([4, 5, 6]), 9)
  test(sum2([4]), 4)

  print ()
  print ('middle_way')
  test(middle_way([1, 2, 3], [4, 5, 6]), [2, 5])
  test(middle_way([7, 7, 7], [3, 8, 0]), [7, 8])
  test(middle_way([5, 2, 9], [1, 4, 5]), [2, 4])
  test(middle_way([1, 9, 7], [4, 8, 8]), [9, 8])
  test(middle_way([1, 2, 3], [3, 1, 4]), [2, 1])
  test(middle_way([1, 2, 3], [4, 1, 1]), [2, 1])
       
  print ()
  print ('date fashion')
  test(date_fashion(5, 10), 2)
  test(date_fashion(5, 2), 0)
  test(date_fashion(5, 5), 1)
  test(date_fashion(3, 3), 1)
  test(date_fashion(10, 2), 0)
  test(date_fashion(2, 9), 0)
  test(date_fashion(9, 9), 2)
  test(date_fashion(10, 5), 2)
  test(date_fashion(2, 2), 0)
  test(date_fashion(3, 7), 1)
  test(date_fashion(2, 7), 0)
  test(date_fashion(6, 2), 0)

  print ()
  print ('squirrel_play')
  test(squirrel_play(70, False), True)
  test(squirrel_play(95, False), False)
  test(squirrel_play(95, True), True)
  test(squirrel_play(90, False), True)
  test(squirrel_play(90, True), True)
  test(squirrel_play(50, False), False)
  test(squirrel_play(50, True), False)
  test(squirrel_play(100, False), False)
  test(squirrel_play(100, True), True)
  test(squirrel_play(105, True), False)
  test(squirrel_play(59, False), False)	
  test(squirrel_play(59, True), False)	
  test(squirrel_play(60, False), True)

  print ()
  print ('Pego correndo')
  test(pego_correndo(60, False), 0)
  test(pego_correndo(65, False), 1)
  test(pego_correndo(65, True), 0)
  test(pego_correndo(80, False), 1)
  test(pego_correndo(85, False), 2)
  test(pego_correndo(85, True), 1)
  test(pego_correndo(70, False), 1)
  test(pego_correndo(75, False), 1)
  test(pego_correndo(75, True), 1)
  test(pego_correndo(40, False), 0)
  test(pego_correndo(40, True), 0)
  test(pego_correndo(90, False), 2)

  print ()
  print ('Alarm Clock')
  test(alarm_clock(1, False), '7:00')
  test(alarm_clock(5, False), '7:00')
  test(alarm_clock(0, False), '10:00')
  test(alarm_clock(6, False), '10:00')
  test(alarm_clock(0, True), 'off')
  test(alarm_clock(6, True), 'off')
  test(alarm_clock(1, True), '10:00')
  test(alarm_clock(3, True), '10:00')
  test(alarm_clock(5, True), '10:00')

if __name__ == '__main__':
  main()
