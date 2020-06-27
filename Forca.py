forca = ['''
  +------+
         |
         |
         |
         |
         |
+--------+ ''', '''
  +------+
  |      |
         |
         |
         |
         |
+--------+ ''', '''
  +------+
  |      |
  o      |
         |
         |
         |
+--------+ ''', '''
  +------+
  |      |
  o      |
  |      |
         |
         |
+--------+ ''', '''
  +------+
  |      |
  o      |
 /|      |
         |
         |
+--------+ ''', '''
  +------+
  |      |
  o      |
 /|\     |
         |
         |
+--------+ ''', '''
  +------+
  |      |
  o      |
 /|\     |
 /       |
         |
+--------+ ''', '''
  +------+
  |      |
  o      |
 /|\     |
 / \     |
         |
+--------+ ''']

certas = erradas = ''
import requests
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
palavras = requests.get(url).text.lower().split()

from random import choice
def escolhe(): return choice(palavras)

def desenha():
    print(forca[len(erradas)])
    for c in sorteada:
        print (c if c in certas else '_', end = ' ')
    print()
    
from string import digits, punctuation
def chute(letras):
  while True:
    x = input('Chute uma letra: ').lower()
    if x in letras:
      print('Repetiu letra')
    elif x in digits + punctuation:
      print('Caracter inválido')
    elif len(x) != 1:
      print('Somente uma letra')
    else:
      return x  

def jogar_novamente():
  return input('Deseja jogar novamente? (SN)').lower() == 's'

def ganhou():
  return set(sorteada) == set(certas)

sorteada = escolhe()
while True:
  desenha()
  x = chute(certas + erradas)
  if x in sorteada: certas = certas + x
  else: erradas = erradas + x
  if len(erradas) == len(forca):
    print(f'Morreu, a palavra era {sorteada}')
    if jogar_novamente():
      certas = erradas = ''
      sorteada = escolhe()
    else: break
  elif ganhou():
    print(f'Acertou a palavra {sorteada}')
    if jogar_novamente():
      certas = erradas = ''
      sorteada = escolhe()
    else: break
    
            
