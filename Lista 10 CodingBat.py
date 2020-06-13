#!/usr/bin/python -tt
# Exercícios by Nick Parlante (CodingBat)

# A. near_ten #
# Seja um n não negativo, retorna True se o número está a distância de
# pelo menos dois de um múltiplo de dez. Use a função resto da divisão.
# near_ten(12) -> True
# near_ten(17) -> False
# near_ten(19) -> True
def near_ten(n):
  return

# B. lone_sum
# Soma maluca: some os números inteiros a, b, e c
# Se algum número aparecer repetido ele não conta na soma
# lone_sum(1, 2, 3) -> 6
# lone_sum(3, 2, 3) -> 2
# lone_sum(3, 3, 3) -> 0
def lone_sum(a, b, c):
  return
# C. luck_sum #
# Soma três inteiros a, b, c
# Se aparecer um 13 ele não conta e todos os da sua direita também
# lucky_sum(1, 2, 3) -> 6
# lucky_sum(1, 2, 13) -> 3
# lucky_sum(1, 13, 3) -> 1
def lucky_sum(a, b, c):
  return
# D. double_char #
# retorna os caracteres da string original duplicados
# double_char('The') -> 'TThhee'
# double_char('AAbb') -> 'AAAAbbbb'
# double_char('Hi-There') -> 'HHii--TThheerree'
def double_char(s):
  return

# E. count_hi #
# conta o número de vezes que aparece a string 'hi'
# count_hi('abc hi ho') -> 1
# count_hi('ABChi hi') -> 2
# count_hi('hihi') -> 2
def count_hi(s):
  return 

# F. cat_dog #
# verifica se o aparece o mesmo número de vezes 'cat' e 'dog'
# cat_dog('catdog') -> True
# cat_dog('catcat') -> False
# cat_dog('1cat1cadodog') -> True
def cat_dog(s):
  return

# G. count_code #
# conta quantas vezes aparece 'code'
# a letra 'd' pode ser trocada por outra qualquer
# assim 'coxe' ou 'coze' também são contadas como 'code'
# count_code('aaacodebbb') -> 1
# count_code('codexxcode') -> 2
# count_code('cozexxcope') -> 2
def count_code(s):
  return 

# H. end_other #
# as duas strings devem ser convertidas para minúsculo via lower()
# depois disso verifique que no final da string b ocorre a string a
# ou se no final da string a ocorre a string b
# end_other('Hiabc', 'abc') -> True
# end_other('AbC', 'HiaBc') -> True
# end_other('abc', 'abXabc') -> True
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if a.endswith(b) or b.endswith(a):
    return True
  return False

# I. count_evens
# conta os números pares da lista
# count_evens([2, 1, 2, 3, 4]) -> 3
# count_evens([2, 2, 0]) -> 3
# count_evens([1, 3, 5]) -> 0
def count_evens(nums):
  count=0
  for k in nums:
    if k % 2 ==0:
      count+=1
  return count

# J. sum13 #
# retorna a soma dos números de uma lista
# 13 dá azar, você deverá ignorar o 13 e todos os números à sua direita
# sum13([1, 2, 2, 1]) -> 6
# sum13([1, 1]) -> 2
# sum13([1, 2, 2, 1, 13]) -> 6
# sum13([13, 1, 2, 3, 4]) -> 0
def sum13(nums):
  if 13 not in nums:
    return sum(nums)

  else:
    k = nums.index(13)
    return sum(nums[:k])
  

# K. has22 #
# Verifica se na lista de números inteiros aparecem dois 2 consecutivos
# has22([1, 2, 2]) -> True
# has22([1, 2, 1, 2]) -> False
# has22([2, 1, 2]) -> False
def has22(nums):
  return '2, 2' in str(nums)
      
  

# L. soma_na_lista #
# Verifica se um número é soma de dois elementos distintos de uma lista
# soma_na_lista(5, [1, 2, 3, 4]) -> True
# soma_na_lista(9, [1, 2, 3, 4]) -> False
# soma_na_lista(0, [1, 2, 3, 4]) -> False
# soma_na_lista(8, [1, 2, 3, 4]) -> False
# soma_na_lista(4, [2, 2, 2, 2]) -> False
# soma_na_lista(4, [2, 2, 1, 3]) -> True
def soma_na_lista(n, lista):
  return

# M.Difícil: Fila de tijolos sem usar loops #
# queremos montar uma fila de tijolos de um tamanho denominado meta
# temos tijolos pequenos (tamanho 1) e tijolos grandes (tamanho 5)
# retorna True se for possível montar a fila de tijolos
# é possível uma solução sem usar for ou while
# fila_tijolos(3, 1, 8) -> True
# fila_tijolos(3, 1, 9) -> False
# fila_tijolos(3, 2, 10) -> True
def fila_tijolos(n_peq, n_gra, meta):
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
  print ('Near_ten')
  test(near_ten(12), True)
  test(near_ten(17), False)
  test(near_ten(19), True)
  test(near_ten(31), True)
  test(near_ten(6), False)
  test(near_ten(10), True)
  test(near_ten(11), True)
  test(near_ten(21), True)
  test(near_ten(22), True)
  test(near_ten(23), False)
  test(near_ten(54), False)
  test(near_ten(155), False)
  test(near_ten(158), True)
  test(near_ten(3), False)
  test(near_ten(1), True)

  print ()
  print ('Lone Sum')
  test(lone_sum(1, 2, 3), 6)
  test(lone_sum(3, 2, 3), 2)
  test(lone_sum(3, 3, 3), 0)
  test(lone_sum(9, 2, 2), 9)
  test(lone_sum(2, 2, 9), 9)
  test(lone_sum(2, 9, 2), 9)
  test(lone_sum(2, 9, 3), 14)
  test(lone_sum(4, 2, 3), 9)
  test(lone_sum(1, 3, 1), 3)

  print ()
  print ('Lucky_sum')
  test(lucky_sum(1, 2, 3), 6)
  test(lucky_sum(1, 2, 13), 3)
  test(lucky_sum(1, 13, 3), 1)
  test(lucky_sum(1, 13, 13), 1)
  test(lucky_sum(6, 5, 2), 13)
  test(lucky_sum(13, 2, 3), 0)
  test(lucky_sum(13, 2, 13), 0)
  test(lucky_sum(13, 13, 2), 0)
  test(lucky_sum(9, 4, 13), 13)
  test(lucky_sum(8, 13, 2), 8)
  test(lucky_sum(7, 2, 1), 10)
  test(lucky_sum(3, 3, 13), 6)

  print ()
  print ('Double_char')
  test(double_char('The'), 'TThhee')
  test(double_char('AAbb'), 'AAAAbbbb')
  test(double_char('Hi-There'), 'HHii--TThheerree')
  test(double_char('Word!'), 'WWoorrdd!!')
  test(double_char('!!'), '!!!!')
  test(double_char(''), '')
  test(double_char('a'), 'aa')
  test(double_char('.'), '..')
  test(double_char('aa'), 'aaaa')

  print ()
  print ('Count_hi')
  test(count_hi('abc hi ho'), 1)
  test(count_hi('ABChi hi'), 2)
  test(count_hi('hihi'), 2)
  test(count_hi('hiHIhi'), 2)
  test(count_hi(''), 0)
  test(count_hi('h'), 0)
  test(count_hi('hi'), 1)
  test(count_hi('Hi is no HI on ahI'), 0)
  test(count_hi('hiho not HOHIhi'), 2)

  print ()
  print ('Cat_dog')
  test(cat_dog('catdog'), True)
  test(cat_dog('catcat'), False)
  test(cat_dog('1cat1cadodog'), True)
  test(cat_dog('catxxdogxxxdog'), False)
  test(cat_dog('catxdogxdogxcat'), True)
  test(cat_dog('catxdogxdogxca'), False)
  test(cat_dog('dogdogcat'), False)
  test(cat_dog('dogogcat'), True)
  test(cat_dog('dog'), False)
  test(cat_dog('cat'), False)
  test(cat_dog('ca'), True)
  test(cat_dog('c'), True)
  test(cat_dog(''), True)

  print ()
  print ('Count_code')
  test(count_code('aaacodebbb'), 1)
  test(count_code('codexxcode'), 2)
  test(count_code('cozexxcope'), 2)
  test(count_code('cozfxxcope'), 1)
  test(count_code('xxcozeyycop'), 1)
  test(count_code('cozcop'), 0)
  test(count_code('abcxyz'), 0)
  test(count_code('code'), 1)
  test(count_code('ode'), 0)
  test(count_code('c'), 0)
  test(count_code(''), 0)
  test(count_code('AAcodeBBcoleCCccoreDD'), 3)
  test(count_code('AAcodeBBcoleCCccorfDD'), 2)
  test(count_code('coAcodeBcoleccoreDD'), 3)

  print ()
  print ('End_other')
  test(end_other('Hiabc', 'abc'), True)
  test(end_other('AbC', 'HiaBc'), True)
  test(end_other('abc', 'abXabc'), True)
  test(end_other('Hiabc', 'abcd'), False)
  test(end_other('Hiabc', 'bc'), True)
  test(end_other('Hiabcx', 'bc'), False)
  test(end_other('abc', 'abc'), True)
  test(end_other('xyz', '12xyz'), True)
  test(end_other('yz', '12xz'), False)
  test(end_other('Z', '12xz'), True)
  test(end_other('12', '12'), True)
  test(end_other('abcXYZ', 'abcDEF'), False)
  test(end_other('ab', 'ab12'), False)
  test(end_other('ab', '12ab'), True)

  print ()
  print ('Count_evens')
  test(count_evens([2, 1, 2, 3, 4]), 3)
  test(count_evens([2, 2, 0]), 3)
  test(count_evens([1, 3, 5]), 0)
  test(count_evens([]), 0)
  test(count_evens([11, 9, 0, 1]), 1)
  test(count_evens([2, 11, 9, 0]), 2)
  test(count_evens([2]), 1)
  test(count_evens([2, 5, 12]), 2)

  print ()
  print ('Sum13')
  test(sum13([1, 2, 2, 1]), 6)
  test(sum13([1, 1]), 2)
  test(sum13([1, 2, 2, 1, 13]), 6)
  test(sum13([1, 2, 13, 2, 1, 13]), 3)
  test(sum13([13, 1, 2, 13, 2, 1, 13]), 0)
  test(sum13([]), 0)
  test(sum13([13]), 0)
  test(sum13([13, 13]), 0)
  test(sum13([13, 0, 13]), 0)
  test(sum13([13, 1, 13]), 0)
  test(sum13([5, 7, 2]), 14)
  test(sum13([5, 13, 2]), 5)
  test(sum13([0]), 0)
  test(sum13([13, 0]), 0)

  print ()
  print ('Has22')
  test(has22([1, 2, 2]), True)
  test(has22([1, 2, 1, 2]), False)
  test(has22([2, 1, 2]), False)
  test(has22([2, 2, 1, 2]), True)
  test(has22([1, 3, 2]), False)
  test(has22([1, 3, 2, 2]), True)
  test(has22([2, 3, 2, 2]), True)
  test(has22([4, 2, 4, 2, 2, 5]), True)
  test(has22([1, 2]), False)
  test(has22([2, 2]), True)
  test(has22([2]), False)
  test(has22([]), False)
  test(has22([3, 3, 2, 2]), True)
  test(has22([5, 2, 5, 2]), False)

  print ()
  print ('Soma na lista')
  test(soma_na_lista(5, [1, 2, 3, 4]), True)
  test(soma_na_lista(9, [1, 2, 3, 4]), False)
  test(soma_na_lista(0, [1, 2, 3, 4]), False)
  test(soma_na_lista(8, [1, 2, 3, 4]), False)
  test(soma_na_lista(4, [2, 2, 2, 2]), False)
  test(soma_na_lista(4, [2, 2, 1, 3]), True)
  test(soma_na_lista(42, [40, 2, 3, 39]), True)

  print ()
  print ('Fila de Tijolos')
  test(fila_tijolos(3, 1, 8), True)
  test(fila_tijolos(3, 1, 9), False)
  test(fila_tijolos(3, 2, 10), True)
  test(fila_tijolos(3, 2, 8), True)
  test(fila_tijolos(3, 2, 9), False)
  test(fila_tijolos(6, 1, 11), True)
  test(fila_tijolos(6, 0, 11), False)
  test(fila_tijolos(3, 1, 7), True)
  test(fila_tijolos(1, 1, 7), False)
  test(fila_tijolos(2, 1, 7), True)
  test(fila_tijolos(7, 1, 11), True)
  test(fila_tijolos(7, 1, 8), True)
  test(fila_tijolos(7, 1, 13), False)
  test(fila_tijolos(43, 1, 46), True)
  test(fila_tijolos(40, 1, 46), False)
  test(fila_tijolos(22, 2, 33), False)
  test(fila_tijolos(0, 2, 10), True)
  test(fila_tijolos(1000000, 1000, 1000100), True)
  test(fila_tijolos(2, 1000000, 100003), False)
  test(fila_tijolos(12, 2, 21), True)

if __name__ == '__main__':
  main()
