#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A. fim_igual
# Dada uma lista de strings, retorna o número de strings
# com tamanho >= 2 onde o primeiro e o último caracteres são iguais
def fim_igual(words):
  k = 0
  for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
      k = k + 1
  return k

# B. x_antes
# Dada uma lista de strings retorna uma lista onde todos os elementos
# que começam com x ficam sorteados antes 
# Exemplo ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] retorna
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Dica: monte duas listas separadas e junte-as no final
def x_antes(words):
  x = []
  outros = []
  for w in words:
    if w.startswith('x'): #w[0] == 'x'
      x.append(w)
    else:
      outros.append(w)
  return sorted(x) + sorted(outros)

# LAB(begin solution)
# Extract the last element from a tuple -- used for custom sorting below.
def last(a):
  return a[-1]
# LAB(end solution)

# C. sort_last
# Dada uma lista de tuplas não vazias retorna uma tupla ordenada
# por ordem crescente do último elemento 
# Exemplo [(1, 7), (1, 3), (3, 4, 5), (2, 2)] retorna
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Dica: use key=função que você definiu e que retorna o último elemento
def sort_last(tuples):
  return sorted(tuples, key=last)

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('fim_igual')
  test(fim_igual(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(fim_igual(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(fim_igual(['aaa', 'be', 'abc', 'hello']), 1)

  print ()
  print ('x_antes')
  test(x_antes(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(x_antes(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(x_antes(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
  print ()
  print ('sort_last')
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()
