#!/usr/bin/python -tt
# Exercícios by Nick Parlante (CodingBat)

# A. multstring
# seja uma string s e um inteiro positivo n
# retorna uma string com n cópias da string original
# multstring('Hi', 2) -> 'HiHi'
def multstring(s, n):
  return 

# B. string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'
def string_splosion(s):
  return 

# C. array_count9
# conta quantas vezes aparece o 9 numa lista nums
def array_count9(nums):
  return

# D. array_front9
# verifica se pelo menos um dos quatro primeiros é nove
# array_front9([1, 2, 9, 3, 4]) -> True
# array_front9([1, 2, 3, 4, 9]) -> False
# array_front9([1, 2, 3, 4, 5]) -> False
def array_front9(nums):
  return

# E. hello_name
# seja uma string name
# hello_name('Bob') -> 'Hello Bob!'
# hello_name('Alice') -> 'Hello Alice!'
# hello_name('X') -> 'Hello X!'
def hello_name(name):
  return

# F. make_tags
# make_tags('i', 'Yay'), '<i>Yay</i>'
# make_tags('i', 'Hello'), '<i>Hello</i>'
# make_tags('cite', 'Yay'), '<cite>Yay</cite>'
def make_tags(tab, word):
  return 

# G. extra_end
# seja um string s com no mínimo duas letras
# retorna três vezes as duas últimas letras
# extra_end('Hello'), 'lololo'
# extra_end('ab'), 'ababab'
# extra_end('Hi'), 'HiHiHi'  
def extra_end(s):
  return 

# H. first_half
# seja uma string s
# retorna a primeira metade da string
# first_half('WooHoo') -> 'Woo'
# first_half('HelloThere') -> 'Hello'
# first_half('abcdef') -> 'abc'
def first_half(s):
  return 

# I. sem_pontas
# seja uma string s de pelo menos dois caracteres
# retorna uma string sem o primeiro e último caracter
# without_end('Hello') -> 'ell'
# without_end('python') -> 'ytho'
# without_end('coding') -> 'odin'
def sem_pontas(s):
  return 

# J. roda2
# rodar uma string s duas posições
# a string possui pelo menos 2 caracteres
# left2('Hello') -> 'lloHe'
# left2('Hi') -> 'Hi'
def roda2(s):
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
  print ('Multstring')
  test(multstring('Hi', 2), 'HiHi')
  test(multstring('Hi', 3), 'HiHiHi')
  test(multstring('Hi', 1), 'Hi')
  test(multstring('Hi', 0), '')
  test(multstring('Hi', 5), 'HiHiHiHiHi')
  test(multstring('Oh Boy!', 2), 'Oh Boy!Oh Boy!')
  test(multstring('x', 4), 'xxxx')
  test(multstring('', 4), '')
  test(multstring('code', 2), 'codecode')
  test(multstring('code', 3), 'codecodecode')

  print ()
  print ('String Explosion')
  test(string_splosion('Code'), 'CCoCodCode')
  test(string_splosion('abc'), 'aababc')
  test(string_splosion('ab'), 'aab')
  test(string_splosion('x'), 'x')
  test(string_splosion('fade'), 'ffafadfade')
  test(string_splosion('There'), 'TThTheTherThere')
  test(string_splosion('Kitten'), 'KKiKitKittKitteKitten')
  test(string_splosion('Bye'), 'BByBye')
  test(string_splosion('Good'), 'GGoGooGood')
  test(string_splosion('Bad'), 'BBaBad')

  print ()
  print ('Array count 9')
  test(array_count9([1, 99, 9]), 1)
  test(array_count9([1, 9, 9]), 2)
  test(array_count9([1, 9, 9, 3, 9]), 3)
  test(array_count9([1, 2, 3]), 0)
  test(array_count9([]), 0)
  test(array_count9([4, 2, 4, 3, 1]), 0)
  test(array_count9([9, 2, 99, 3, 1]), 1)
  
  print ()
  print ('Array front 9')
  test(array_front9([1, 2, 9, 3, 4]), True)
  test(array_front9([1, 2, 3, 4, 9]), False)
  test(array_front9([1, 2, 3, 4, 5]), False)
  test(array_front9([9, 2, 3]), True)
  test(array_front9([1, 9, 9]), True)
  test(array_front9([1, 2, 3]), False)
  test(array_front9([1, 9]), True)
  test(array_front9([5, 5]), False)
  test(array_front9([2]), False)
  test(array_front9([9]), True)
  test(array_front9([]), False)
  test(array_front9([3, 9, 2, 3, 3]), True)

  print ()
  print ('Hello Name')
  test(hello_name('Bob'), 'Hello Bob!')
  test(hello_name('Alice'), 'Hello Alice!')
  test(hello_name('X'), 'Hello X!')
  test(hello_name('Hello'), 'Hello Hello!')

  print ()
  print ('Make Tags')
  test(make_tags('i', 'Yay'), '<i>Yay</i>')
  test(make_tags('i', 'Hello'), '<i>Hello</i>')
  test(make_tags('cite', 'Yay'), '<cite>Yay</cite>')
  test(make_tags('address', 'here'), '<address>here</address>')
  test(make_tags('body', 'Heart'), '<body>Heart</body>')
  test(make_tags('i', 'i'), '<i>i</i>')
  test(make_tags('i', ''), '<i></i>')

  print ()
  print ('Extra End')
  test(extra_end('Hello'), 'lololo')
  test(extra_end('ab'), 'ababab')
  test(extra_end('Hi'), 'HiHiHi')
  test(extra_end('Candy'), 'dydydy')
  test(extra_end('Code'), 'dedede')

  print ()
  print ('First Half')
  test(first_half('WooHoo'), 'Woo')
  test(first_half('HelloThere'), 'Hello')
  test(first_half('abcdef'), 'abc')
  test(first_half('ab'), 'a')
  test(first_half(''), '')
  test(first_half('0123456789'), '01234')
  test(first_half('kitten'), 'kit')

  print ()
  print ('Sem Pontas')
  test(sem_pontas('Hello'), 'ell')
  test(sem_pontas('Python'), 'ytho')
  test(sem_pontas('coding'), 'odin')
  test(sem_pontas('code'), 'od')
  test(sem_pontas('ab'), '')
  test(sem_pontas('Chocolate!'), 'hocolate')
  test(sem_pontas('kitten'), 'itte')
  test(sem_pontas('woohoo'), 'ooho')

  print ()
  print ('Roda 2')
  test(roda2('Hello'), 'lloHe')
  test(roda2('python'), 'thonpy')
  test(roda2('Hi'), 'Hi')
  test(roda2('code'), 'deco')
  test(roda2('cat'), 'tca')
  test(roda2('12345'), '34512')
  test(roda2('Chocolate'), 'ocolateCh')
  test(roda2('bricks'), 'icksbr')

if __name__ == '__main__':
  main()
