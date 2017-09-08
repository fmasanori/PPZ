# Esta provinha deve ser feita em Python 3
# Procure utilizar alguma IDE que permita caracteres especiais
# Repare que o IDLE para Python 3 já faz isso
# Você poderá consultar suas anotações pessoais ou
# qualquer documentação sobre a sintaxe do Python
# e suas bibliotecas. No entanto não será permitida
# a consulta dos vídeos explicando as listas e nem
# o código fonte de sua resolução, seja qual for sua origem
# Boa sorte! A pontuação mínima é de 60 pontos

# alô_mundo
# retorne 'Alô Mundo' para não ficar com zero na provinha
def alô_mundo():
  return 'Alô Mundo'

# chinês
# converta uma string msg para chinês
# para isso faça um deslocamento de 30000 em cada caracter
# chinês('Zumbi') -> '疊疥疝疒疙'
def chinês(msg):
  s = ''
  for c in msg: s += chr(ord(c) + 30000)
  return s

# anagrama
# verifique se duas strings s1 e s2 são anagramas
# anagrama('aberto', 'rebato') -> True
# anagrama('roma', 'amor') -> True
# anagrama('asa', 'assa') -> False
# é possível uma solução com uma única linha
def anagrama(s1, s2):
  return sorted(s1) == sorted(s2)

# loja_tinta
# suponha que uma lata pinte 54 metros quadrados
# dada a metragem em metros quadrados (inteiro positivo)
# retorne quantas latas são necessárias
# loja_tinta(54) -> 1
# loja_tinta(60) -> 2
# loja_tinta(108) -> 2
# loja_tinta(109) -> 3
def loja_tinta(m):
  latas = m // 54
  if m % 54 != 0:
    return latas + 1
  else:
    return latas
  
# alunos_problema
# temos dois alunos a e b
# a_sorri e b_sorri indicam se a e b sorriem
# temos problemas quando ambos estão sorrindo ou ambos
# não estão sorrindo
# retorne True quando houver problemas
def alunos_problema(a_sorri, b_sorri):
  return a_sorri == b_sorri

# papagaio
# temos um papagaio que fala alto
# hora é um parâmetro entre 0 e 23
# temos problemas se o papagaio estiver falando
# antes da 7 ou depois das 20
def papagaio(falando, hora):
  return falando and (hora < 7 or hora > 20)

# apaga
# seja uma string s e um inteiro n
# retorna uma nova string sem a posição n
# apaga('kitten', 1) -> 'ktten'
# apaga('kitten', 4) -> 'kittn'
def apaga(s, n):
  return s[:n] + s[n+1:]

# troca
# seja uma string s
# se s tiver tamanho <= 1 retorna ela mesma
# caso contrário troca a primeira e última letra
# troca('code') -> 'eodc'
# troca('a') -> 'a'
# troca('ab') -> 'ba'
def troca(s):
  return s if len(s) <= 1 else s[-1] + s[1:-1] + s[0]

# string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'
def string_splosion(s):
  return ''.join([s[:k] for k in range(len(s) + 1)])
  resp = ''
  for k in range(len(s)):
    resp += s[:k]
  resp += s
  return resp

# make_tags
# make_tags('i', 'Yay'), '<i>Yay</i>'
# make_tags('i', 'Hello'), '<i>Hello</i>'
# make_tags('cite', 'Yay'), '<cite>Yay</cite>'
def make_tags(tag, word):
  return '<%s>%s</%s>' %(tag, word, tag)

# roda2
# rodar uma string s duas posições
# a string possui pelo menos 2 caracteres
# left2('Hello') -> 'lloHe'
# left2('Hi') -> 'Hi'
def roda2(s):
  return s[2:] + s[:2]

# date_fashion
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
  if eu <= 2 or par <= 2:
    return 0
  if eu >= 8 or par >= 8:
    return 2
  return 1

# squirrel_play
# os esquilos na FATEC brincam quando a temperatura está entre 60 e 90
# graus Fahreneit (são estrangeiros e o termômetro é diferente rs)
# caso seja verão, então a temperatura superior é 100 no lugar de 90
# retorne True caso os esquilos brinquem
# squirrel_play(70, False) -> True
# squirrel_play(95, False) -> False
# squirrel_play(95, True) -> True
def squirrel_play(temp, is_summer):
  return 60 <= temp <= 100 if is_summer else 60 <= temp <= 90

# pego_correndo
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
  if is_birthday:
    speed -= 5
  if speed <= 60:
    return 0
  if 61 <= speed <= 80:
    return 1
  return 2

# count_code
# conta quantas vezes aparece 'code'
# a letra 'd' pode ser trocada por outra qualquer
# assim 'coxe' ou 'coze' também são contadas como 'code'
# count_code('aaacodebbb') -> 1
# count_code('codexxcode') -> 2
# count_code('cozexxcope') -> 2
def count_code(s):
  cont = 0
  for k in range(len(s)-3):
    if s[k:k+2] == 'co' and s[k+3] == 'e':
      cont += 1
  return cont

# Fila de tijolos sem usar loops
# queremos montar uma fila de tijolos de um tamanho denominado meta
# temos tijolos pequenos (tamanho 1) e tijolos grandes (tamanho 5)
# retorna True se for possível montar a fila de tijolos
# programe uma solução sem usar for ou while
# fila_tijolos(3, 1, 8) -> True
# fila_tijolos(3, 1, 9) -> False
# fila_tijolos(3, 2, 10) -> True
def fila_tijolos(n_peq, n_gra, meta):
  return n_peq >= meta % 5 and n_peq + 5 * n_gra >= meta

# busca (COMP 89 IME-USP)
# Verifique quantas ocorrências de uma palavra há numa frase
# frase = 'ana e mariana gostam de banana'
# palavra = 'ana'
# busca ('ana e mariana gostam de banana', 'ana') == 4
# Hall of Fame Victor H. Panisa, 1a turma Python para Zumbis
def busca(frase, palavra):
  return len([k for k in range(len(frase))
              if frase[k:len(palavra)+k] == palavra])

# zeros finais
# Verifique quantos zeros há no final de um número inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui três
def zf(n):
  n = str(n)[::-1]
  k = 0
  while n[k] == '0':
    k = k + 1
  return k
  a = int(str(n)[::-1])
  return len(str(n)) - len(str(a))

# conta 2
# Verifique quantas vezes o dígito 2 aparece entre 0 e n-1
# Exemplo: para n = 20 o dígito 2 aparece duas vezes entre 0 e 19
def conta2(n):
  s = ''
  for i in range(n):
    s = s + str(i)
  return s.count('2')

# inicio em potencia de 2
# Dado um número inteiro positivo n retorne a primeira potência de 2
# que tenha o início igual a n
# Exemplo: para n = 65 retornará 16 pois 2**16 = 65536
def inip2(n):
  k = 0
  while True:
    pot = str(2**k)
    if pot.startswith(str(n)):
      return k
    k = k + 1

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(obtido, esperado):
  return obtido == esperado

def main():
  pontos = 5 if alô_mundo() == 'Alô Mundo' else 0

  if all([
  test(chinês('Zumbi'), '疊疥疝疒疙'),
  test(chinês('batatinha'), '疒疑疤疑疤疙疞疘疑'),
  test(chinês('Python'), '疀疩疤疘疟疞'),
  test(chinês('PyLadies'), '疀疩畼疑疔疙疕疣')]):
    pontos += 5

  if all([
  test(anagrama('aberto', 'rebato'), True),
  test(anagrama('amor', 'roma'), True),
  test(anagrama('ramo', 'amor'), True),
  test(anagrama('asa', 'assa'), False),
  test(anagrama('', 'casa'), False)]):
    pontos += 5

  if all([
  test(loja_tinta(50), 1),
  test(loja_tinta(54), 1),
  test(loja_tinta(55), 2),
  test(loja_tinta(108), 2),
  test(loja_tinta(109), 3),
  test(loja_tinta(162), 3)]):
    pontos += 5

  if all([
  test(alunos_problema(True, True), True),
  test(alunos_problema(False, False), True),
  test(alunos_problema(True, False), False),
  test(alunos_problema(False, True), False)]):
    pontos += 5

  if all([
  test(papagaio(True, 6), True),
  test(papagaio(True, 7), False),
  test(papagaio(False, 6), False),
  test(papagaio(True, 21), True),
  test(papagaio(False, 21), False),
  test(papagaio(True, 23), True),
  test(papagaio(True, 20), False)]):
    pontos += 5
    
  if all([
  test(apaga('kitten', 1), 'ktten'),
  test(apaga('kitten', 0), 'itten'), 
  test(apaga('kitten', 4), 'kittn'),
  test(apaga('Hi', 0), 'i'),
  test(apaga('Hi', 1), 'H'),
  test(apaga('code', 0), 'ode'),
  test(apaga('code', 1), 'cde'),
  test(apaga('code', 2), 'coe'),
  test(apaga('code', 3), 'cod'),
  test(apaga('chocolate', 8), 'chocolat')]):
    pontos += 5
    
  if all([
  test(troca('code'), 'eodc'),	    
  test(troca('a'), 'a'),
  test(troca('ab'), 'ba'),
  test(troca('abc'), 'cba'),
  test(troca(''), ''),
  test(troca('Chocolate'), 'ehocolatC'),
  test(troca('nythoP'), 'Python'),
  test(troca('hello'), 'oellh')]):
    pontos += 5

  if all([
  test(string_splosion('Code'), 'CCoCodCode'),
  test(string_splosion('abc'), 'aababc'),
  test(string_splosion('ab'), 'aab'),
  test(string_splosion('x'), 'x'),
  test(string_splosion('fade'), 'ffafadfade'),
  test(string_splosion('There'), 'TThTheTherThere'),
  test(string_splosion('Kitten'), 'KKiKitKittKitteKitten'),
  test(string_splosion('Bye'), 'BByBye'),
  test(string_splosion('Good'), 'GGoGooGood'),
  test(string_splosion('Bad'), 'BBaBad')]):
    pontos += 5
    
  if all([
  test(make_tags('i', 'Yay'), '<i>Yay</i>'),
  test(make_tags('i', 'Hello'), '<i>Hello</i>'),
  test(make_tags('cite', 'Yay'), '<cite>Yay</cite>'),
  test(make_tags('address', 'here'), '<address>here</address>'),
  test(make_tags('body', 'Heart'), '<body>Heart</body>'),
  test(make_tags('i', 'i'), '<i>i</i>'),
  test(make_tags('i', ''), '<i></i>')]):
    pontos += 5

  if all([
  test(roda2('Hello'), 'lloHe'),
  test(roda2('python'), 'thonpy'),
  test(roda2('Hi'), 'Hi'),
  test(roda2('code'), 'deco'),
  test(roda2('cat'), 'tca'),
  test(roda2('12345'), '34512'),
  test(roda2('Chocolate'), 'ocolateCh'),
  test(roda2('bricks'), 'icksbr')]):
    pontos += 5

  if all([
  test(date_fashion(5, 10), 2),
  test(date_fashion(5, 2), 0),
  test(date_fashion(5, 5), 1),
  test(date_fashion(3, 3), 1),
  test(date_fashion(10, 2), 0),
  test(date_fashion(2, 9), 0),
  test(date_fashion(9, 9), 2),
  test(date_fashion(10, 5), 2),
  test(date_fashion(2, 2), 0),
  test(date_fashion(3, 7), 1),
  test(date_fashion(2, 7), 0),
  test(date_fashion(6, 2), 0)]):
    pontos += 5

  if all([
  test(squirrel_play(70, False), True),
  test(squirrel_play(95, False), False),
  test(squirrel_play(95, True), True),
  test(squirrel_play(90, False), True),
  test(squirrel_play(90, True), True),
  test(squirrel_play(50, False), False),
  test(squirrel_play(50, True), False),
  test(squirrel_play(100, False), False),
  test(squirrel_play(100, True), True),
  test(squirrel_play(105, True), False),
  test(squirrel_play(59, False), False),
  test(squirrel_play(59, True), False),	
  test(squirrel_play(60, False), True)]):
    pontos += 5

  if all([
  test(pego_correndo(60, False), 0),
  test(pego_correndo(65, False), 1),
  test(pego_correndo(65, True), 0),
  test(pego_correndo(80, False), 1),
  test(pego_correndo(85, False), 2),
  test(pego_correndo(85, True), 1),
  test(pego_correndo(70, False), 1),
  test(pego_correndo(75, False), 1),
  test(pego_correndo(75, True), 1),
  test(pego_correndo(40, False), 0),
  test(pego_correndo(40, True), 0),
  test(pego_correndo(90, False), 2)]):
    pontos += 5

  if all([
  test(count_code('aaacodebbb'), 1),
  test(count_code('codexxcode'), 2),
  test(count_code('cozexxcope'), 2),
  test(count_code('cozfxxcope'), 1),
  test(count_code('xxcozeyycop'), 1),
  test(count_code('cozcop'), 0),
  test(count_code('abcxyz'), 0),
  test(count_code('code'), 1),
  test(count_code('ode'), 0),
  test(count_code('c'), 0),
  test(count_code(''), 0),
  test(count_code('AAcodeBBcoleCCccoreDD'), 3),
  test(count_code('AAcodeBBcoleCCccorfDD'), 2),
  test(count_code('coAcodeBcoleccoreDD'), 3)]):
    pontos += 5

  if all([
  test(fila_tijolos(3, 1, 8), True),
  test(fila_tijolos(3, 1, 9), False),
  test(fila_tijolos(3, 2, 10), True),
  test(fila_tijolos(3, 2, 8), True),
  test(fila_tijolos(3, 2, 9), False),
  test(fila_tijolos(6, 1, 11), True),
  test(fila_tijolos(6, 0, 11), False),
  test(fila_tijolos(3, 1, 7), True),
  test(fila_tijolos(1, 1, 7), False),
  test(fila_tijolos(2, 1, 7), True),
  test(fila_tijolos(7, 1, 11), True),
  test(fila_tijolos(7, 1, 8), True),
  test(fila_tijolos(7, 1, 13), False),
  test(fila_tijolos(43, 1, 46), True),
  test(fila_tijolos(40, 1, 46), False),
  test(fila_tijolos(22, 2, 33), False),
  test(fila_tijolos(0, 2, 10), True),
  test(fila_tijolos(1000000, 1000, 1000100), True),
  test(fila_tijolos(2, 1000000, 100003), False),
  test(fila_tijolos(12, 2, 21), True)]):
    pontos += 5

  if all([
  test(busca('ana e mariana gostam de banana', 'ana'), 4),
  test(busca('uma arara ou duas araras', 'ara'), 4),
  test(busca('asasasasasasasa', 'asa'), 7)]):
    pontos += 5

  if all([
  test(zf(10100100010000), 4),
  test(zf(90000000000000000010), 1)]):
    pontos += 5

  if all([
  test(conta2(20), 2),
  test(conta2(999), 300),
  test(conta2(555), 216)]):
    pontos += 5

  if all([
  test(inip2(7), 46),
  test(inip2(133), 316),
  test(inip2(1024), 10)]):
    pontos += 5

  print ('Pontos: %d/100' %pontos)
  
if __name__ == '__main__':
  main()
