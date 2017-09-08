# Prova Final do PPZ. Prazo de entrega: meia noite do dia  31 de agosto.
# Esta provinha deve ser feita em Python 3.  Procure utilizar alguma IDE
# que permita caracteres especiais. O IDLE do Python 3 é suficiente para
# isso. Você poderá  consultar  suas anotações pessoais ou qualquer docu-
# mentação sobre a sintaxe do Python  e suas bibliotecas. No entanto não
# será permitida a consulta dos vídeos explicando as listas e  nem do có-
# digo fonte de sua resolução, seja qual for sua origem. A pontuação mí-
# nima é de 60 pontos. Boa sorte! Obs: a identação abaixo é de 2 espaços
# ATENÇÃO: sempre visando o aprendizado do aluno não será tolerado o plá-
# gio. Caso você queira trocar alguma ideia com um colega, faça isso ape-
# nas verbalmente e de forma genérica, sem  troca de código, no fórum de
# discussão. Certifique-se  de  construir  as  respostas  desde  o zero,
# copiando você não irá aprender, que é o que realmente importa no curso.
# O código sangrando ou em Python 2.x não poderá ser processado pelo nos-
# so script de correção automática. Entregue um único código fonte. Cada
# questão vale 5 pontos. Lembre  que você  poderá enviar seu código, com
# suas dúvidas para socorro@pycursos.com e  receberá ajuda. Somos poucos
# para responder, portanto  talvez a resposta não seja imediata, aguarde,
# por favor. Novamente boa sorte e bom aprendizado!

# alô_mundo
# retorne 'Alô Mundo' para não ficar com zero na provinha
def alô_mundo():
  return 

# chinês
# converta uma string msg para chinês
# para isso faça um deslocamento de 30000 em cada caracter
# chinês('Zumbi') -> '疊疥疝疒疙'
def chinês(msg):
  return 

# anagrama
# verifique se duas strings s1 e s2 são anagramas
# anagrama('aberto', 'rebato') -> True
# anagrama('roma', 'amor') -> True
# anagrama('asa', 'assa') -> False
# é possível uma solução com uma única linha
def anagrama(s1, s2):
  return 

# loja_tinta
# suponha que uma lata pinte 54 metros quadrados
# dada a metragem em metros quadrados (inteiro positivo)
# retorne quantas latas são necessárias
# loja_tinta(54) -> 1
# loja_tinta(60) -> 2
# loja_tinta(108) -> 2
# loja_tinta(109) -> 3
def loja_tinta(m):
  return

# alunos_problema
# temos dois alunos a e b
# a_sorri e b_sorri indicam se a e b sorriem
# temos problemas quando ambos estão sorrindo ou ambos
# não estão sorrindo
# retorne True quando houver problemas
def alunos_problema(a_sorri, b_sorri):
  return 

# papagaio
# temos um papagaio que fala alto
# hora é um parâmetro entre 0 e 23
# temos problemas se o papagaio estiver falando
# antes da 7 ou depois das 20
def papagaio(falando, hora):
  return 

# apaga
# seja uma string s e um inteiro n
# retorna uma nova string sem a posição n
# apaga('kitten', 1) -> 'ktten'
# apaga('kitten', 4) -> 'kittn'
def apaga(s, n):
  return 

# troca
# seja uma string s
# se s tiver tamanho <= 1 retorna ela mesma
# caso contrário troca a primeira e última letra
# troca('code') -> 'eodc'
# troca('a') -> 'a'
# troca('ab') -> 'ba'
def troca(s):
  return 

# string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'
def string_splosion(s):
  return 

# make_tags
# make_tags('i', 'Yay'), '<i>Yay</i>'
# make_tags('i', 'Hello'), '<i>Hello</i>'
# make_tags('cite', 'Yay'), '<cite>Yay</cite>'
def make_tags(tag, word):
  return 

# roda2
# rodar uma string s duas posições
# a string possui pelo menos 2 caracteres
# left2('Hello') -> 'lloHe'
# left2('Hi') -> 'Hi'
def roda2(s):
  return 

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
  return 

# squirrel_play
# os esquilos na FATEC brincam quando a temperatura está entre 60 e 90
# graus Fahreneit (são estrangeiros e o termômetro é diferente rs)
# caso seja verão, então a temperatura superior é 100 no lugar de 90
# retorne True caso os esquilos brinquem
# squirrel_play(70, False) -> True
# squirrel_play(95, False) -> False
# squirrel_play(95, True) -> True
def squirrel_play(temp, is_summer):
  return 

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
  return

# count_code
# conta quantas vezes aparece 'code'
# a letra 'd' pode ser trocada por outra qualquer
# assim 'coxe' ou 'coze' também são contadas como 'code'
# count_code('aaacodebbb') -> 1
# count_code('codexxcode') -> 2
# count_code('cozexxcope') -> 2
def count_code(s):
  return

# Fila de tijolos sem usar loops
# queremos montar uma fila de tijolos de um tamanho denominado meta
# temos tijolos pequenos (tamanho 1) e tijolos grandes (tamanho 5)
# retorna True se for possível montar a fila de tijolos
# programe uma solução sem usar for ou while
# fila_tijolos(3, 1, 8) -> True
# fila_tijolos(3, 1, 9) -> False
# fila_tijolos(3, 2, 10) -> True
def fila_tijolos(n_peq, n_gra, meta):
  return

# busca (COMP 89 IME-USP)
# Verifique quantas ocorrências de uma palavra há numa frase
# frase = 'ana e mariana gostam de banana'
# palavra = 'ana'
# busca ('ana e mariana gostam de banana', 'ana') == 4
def busca(frase, palavra):
  return

# zeros finais
# Verifique quantos zeros há no final de um número inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui três
# Dica: talvez converter para string torne o exercício mais fácil
def zf(n):
  return

# conta 2
# Verifique quantas vezes o dígito 2 aparece entre 0 e n-1
# Exemplo: para n = 20 o dígito 2 aparece duas vezes entre 0 e 19
def conta2(n):
  return

# inicio em potencia de 2
# Dado um número inteiro positivo n retorne a primeira potência de 2
# que tenha o início igual a n
# Exemplo: para n = 65 retornará 16 pois 2**16 = 65536
def inip2(n):
  return

# O código abaixo avalia suas questões, favor não alterar ou decodificar
from base64 import b64decode
code = b'IyBQcm92aWRlZCBzaW1wbGUgdGVzdCgpIGZ1bmN0aW9uIHVzZWQgaW4gbWFpbigpIHRvIHByaW50CiMgd2hhdCBlYWNoIGZ1bmN0aW9uIHJldHVybnMgdnMuIHdoYXQgaXQncyBzdXBwb3NlZCB0byByZXR1cm4uCmRlZiB0ZXN0KG9idGlkbywgZXNwZXJhZG8pOgogIHJldHVybiBvYnRpZG8gPT0gZXNwZXJhZG8KCmRlZiBtYWluKCk6CiAgcG9udG9zID0gNSBpZiBhbMO0X211bmRvKCkgPT0gJ0Fsw7QgTXVuZG8nIGVsc2UgMAoKICBpZiBhbGwoWwogIHRlc3QoY2hpbsOqcygnWnVtYmknKSwgJ+eWiueWpeeWneeWkueWmScpLAogIHRlc3QoY2hpbsOqcygnYmF0YXRpbmhhJyksICfnlpLnlpHnlqTnlpHnlqTnlpnnlp7nlpjnlpEnKSwKICB0ZXN0KGNoaW7DqnMoJ1B5dGhvbicpLCAn55aA55ap55ak55aY55af55aeJyksCiAgdGVzdChjaGluw6pzKCdQeUxhZGllcycpLCAn55aA55ap55W855aR55aU55aZ55aV55ajJyldKToKICAgIHBvbnRvcyArPSA1CgogIGlmIGFsbChbCiAgdGVzdChhbmFncmFtYSgnYWJlcnRvJywgJ3JlYmF0bycpLCBUcnVlKSwKICB0ZXN0KGFuYWdyYW1hKCdhbW9yJywgJ3JvbWEnKSwgVHJ1ZSksCiAgdGVzdChhbmFncmFtYSgncmFtbycsICdhbW9yJyksIFRydWUpLAogIHRlc3QoYW5hZ3JhbWEoJ2FzYScsICdhc3NhJyksIEZhbHNlKSwKICB0ZXN0KGFuYWdyYW1hKCcnLCAnY2FzYScpLCBGYWxzZSldKToKICAgIHBvbnRvcyArPSA1CgogIGlmIGFsbChbCiAgdGVzdChsb2phX3RpbnRhKDUwKSwgMSksCiAgdGVzdChsb2phX3RpbnRhKDU0KSwgMSksCiAgdGVzdChsb2phX3RpbnRhKDU1KSwgMiksCiAgdGVzdChsb2phX3RpbnRhKDEwOCksIDIpLAogIHRlc3QobG9qYV90aW50YSgxMDkpLCAzKSwKICB0ZXN0KGxvamFfdGludGEoMTYyKSwgMyldKToKICAgIHBvbnRvcyArPSA1CgogIGlmIGFsbChbCiAgdGVzdChhbHVub3NfcHJvYmxlbWEoVHJ1ZSwgVHJ1ZSksIFRydWUpLAogIHRlc3QoYWx1bm9zX3Byb2JsZW1hKEZhbHNlLCBGYWxzZSksIFRydWUpLAogIHRlc3QoYWx1bm9zX3Byb2JsZW1hKFRydWUsIEZhbHNlKSwgRmFsc2UpLAogIHRlc3QoYWx1bm9zX3Byb2JsZW1hKEZhbHNlLCBUcnVlKSwgRmFsc2UpXSk6CiAgICBwb250b3MgKz0gNQoKICBpZiBhbGwoWwogIHRlc3QocGFwYWdhaW8oVHJ1ZSwgNiksIFRydWUpLAogIHRlc3QocGFwYWdhaW8oVHJ1ZSwgNyksIEZhbHNlKSwKICB0ZXN0KHBhcGFnYWlvKEZhbHNlLCA2KSwgRmFsc2UpLAogIHRlc3QocGFwYWdhaW8oVHJ1ZSwgMjEpLCBUcnVlKSwKICB0ZXN0KHBhcGFnYWlvKEZhbHNlLCAyMSksIEZhbHNlKSwKICB0ZXN0KHBhcGFnYWlvKFRydWUsIDIzKSwgVHJ1ZSksCiAgdGVzdChwYXBhZ2FpbyhUcnVlLCAyMCksIEZhbHNlKV0pOgogICAgcG9udG9zICs9IDUKICAgIAogIGlmIGFsbChbCiAgdGVzdChhcGFnYSgna2l0dGVuJywgMSksICdrdHRlbicpLAogIHRlc3QoYXBhZ2EoJ2tpdHRlbicsIDApLCAnaXR0ZW4nKSwgCiAgdGVzdChhcGFnYSgna2l0dGVuJywgNCksICdraXR0bicpLAogIHRlc3QoYXBhZ2EoJ0hpJywgMCksICdpJyksCiAgdGVzdChhcGFnYSgnSGknLCAxKSwgJ0gnKSwKICB0ZXN0KGFwYWdhKCdjb2RlJywgMCksICdvZGUnKSwKICB0ZXN0KGFwYWdhKCdjb2RlJywgMSksICdjZGUnKSwKICB0ZXN0KGFwYWdhKCdjb2RlJywgMiksICdjb2UnKSwKICB0ZXN0KGFwYWdhKCdjb2RlJywgMyksICdjb2QnKSwKICB0ZXN0KGFwYWdhKCdjaG9jb2xhdGUnLCA4KSwgJ2Nob2NvbGF0JyldKToKICAgIHBvbnRvcyArPSA1CiAgICAKICBpZiBhbGwoWwogIHRlc3QodHJvY2EoJ2NvZGUnKSwgJ2VvZGMnKSwJICAgIAogIHRlc3QodHJvY2EoJ2EnKSwgJ2EnKSwKICB0ZXN0KHRyb2NhKCdhYicpLCAnYmEnKSwKICB0ZXN0KHRyb2NhKCdhYmMnKSwgJ2NiYScpLAogIHRlc3QodHJvY2EoJycpLCAnJyksCiAgdGVzdCh0cm9jYSgnQ2hvY29sYXRlJyksICdlaG9jb2xhdEMnKSwKICB0ZXN0KHRyb2NhKCdueXRob1AnKSwgJ1B5dGhvbicpLAogIHRlc3QodHJvY2EoJ2hlbGxvJyksICdvZWxsaCcpXSk6CiAgICBwb250b3MgKz0gNQoKICBpZiBhbGwoWwogIHRlc3Qoc3RyaW5nX3NwbG9zaW9uKCdDb2RlJyksICdDQ29Db2RDb2RlJyksCiAgdGVzdChzdHJpbmdfc3Bsb3Npb24oJ2FiYycpLCAnYWFiYWJjJyksCiAgdGVzdChzdHJpbmdfc3Bsb3Npb24oJ2FiJyksICdhYWInKSwKICB0ZXN0KHN0cmluZ19zcGxvc2lvbigneCcpLCAneCcpLAogIHRlc3Qoc3RyaW5nX3NwbG9zaW9uKCdmYWRlJyksICdmZmFmYWRmYWRlJyksCiAgdGVzdChzdHJpbmdfc3Bsb3Npb24oJ1RoZXJlJyksICdUVGhUaGVUaGVyVGhlcmUnKSwKICB0ZXN0KHN0cmluZ19zcGxvc2lvbignS2l0dGVuJyksICdLS2lLaXRLaXR0S2l0dGVLaXR0ZW4nKSwKICB0ZXN0KHN0cmluZ19zcGxvc2lvbignQnllJyksICdCQnlCeWUnKSwKICB0ZXN0KHN0cmluZ19zcGxvc2lvbignR29vZCcpLCAnR0dvR29vR29vZCcpLAogIHRlc3Qoc3RyaW5nX3NwbG9zaW9uKCdCYWQnKSwgJ0JCYUJhZCcpXSk6CiAgICBwb250b3MgKz0gNQogICAgCiAgaWYgYWxsKFsKICB0ZXN0KG1ha2VfdGFncygnaScsICdZYXknKSwgJzxpPllheTwvaT4nKSwKICB0ZXN0KG1ha2VfdGFncygnaScsICdIZWxsbycpLCAnPGk+SGVsbG88L2k+JyksCiAgdGVzdChtYWtlX3RhZ3MoJ2NpdGUnLCAnWWF5JyksICc8Y2l0ZT5ZYXk8L2NpdGU+JyksCiAgdGVzdChtYWtlX3RhZ3MoJ2FkZHJlc3MnLCAnaGVyZScpLCAnPGFkZHJlc3M+aGVyZTwvYWRkcmVzcz4nKSwKICB0ZXN0KG1ha2VfdGFncygnYm9keScsICdIZWFydCcpLCAnPGJvZHk+SGVhcnQ8L2JvZHk+JyksCiAgdGVzdChtYWtlX3RhZ3MoJ2knLCAnaScpLCAnPGk+aTwvaT4nKSwKICB0ZXN0KG1ha2VfdGFncygnaScsICcnKSwgJzxpPjwvaT4nKV0pOgogICAgcG9udG9zICs9IDUKCiAgaWYgYWxsKFsKICB0ZXN0KHJvZGEyKCdIZWxsbycpLCAnbGxvSGUnKSwKICB0ZXN0KHJvZGEyKCdweXRob24nKSwgJ3Rob25weScpLAogIHRlc3Qocm9kYTIoJ0hpJyksICdIaScpLAogIHRlc3Qocm9kYTIoJ2NvZGUnKSwgJ2RlY28nKSwKICB0ZXN0KHJvZGEyKCdjYXQnKSwgJ3RjYScpLAogIHRlc3Qocm9kYTIoJzEyMzQ1JyksICczNDUxMicpLAogIHRlc3Qocm9kYTIoJ0Nob2NvbGF0ZScpLCAnb2NvbGF0ZUNoJyksCiAgdGVzdChyb2RhMignYnJpY2tzJyksICdpY2tzYnInKV0pOgogICAgcG9udG9zICs9IDUKCiAgaWYgYWxsKFsKICB0ZXN0KGRhdGVfZmFzaGlvbig1LCAxMCksIDIpLAogIHRlc3QoZGF0ZV9mYXNoaW9uKDUsIDIpLCAwKSwKICB0ZXN0KGRhdGVfZmFzaGlvbig1LCA1KSwgMSksCiAgdGVzdChkYXRlX2Zhc2hpb24oMywgMyksIDEpLAogIHRlc3QoZGF0ZV9mYXNoaW9uKDEwLCAyKSwgMCksCiAgdGVzdChkYXRlX2Zhc2hpb24oMiwgOSksIDApLAogIHRlc3QoZGF0ZV9mYXNoaW9uKDksIDkpLCAyKSwKICB0ZXN0KGRhdGVfZmFzaGlvbigxMCwgNSksIDIpLAogIHRlc3QoZGF0ZV9mYXNoaW9uKDIsIDIpLCAwKSwKICB0ZXN0KGRhdGVfZmFzaGlvbigzLCA3KSwgMSksCiAgdGVzdChkYXRlX2Zhc2hpb24oMiwgNyksIDApLAogIHRlc3QoZGF0ZV9mYXNoaW9uKDYsIDIpLCAwKV0pOgogICAgcG9udG9zICs9IDUKCiAgaWYgYWxsKFsKICB0ZXN0KHNxdWlycmVsX3BsYXkoNzAsIEZhbHNlKSwgVHJ1ZSksCiAgdGVzdChzcXVpcnJlbF9wbGF5KDk1LCBGYWxzZSksIEZhbHNlKSwKICB0ZXN0KHNxdWlycmVsX3BsYXkoOTUsIFRydWUpLCBUcnVlKSwKICB0ZXN0KHNxdWlycmVsX3BsYXkoOTAsIEZhbHNlKSwgVHJ1ZSksCiAgdGVzdChzcXVpcnJlbF9wbGF5KDkwLCBUcnVlKSwgVHJ1ZSksCiAgdGVzdChzcXVpcnJlbF9wbGF5KDUwLCBGYWxzZSksIEZhbHNlKSwKICB0ZXN0KHNxdWlycmVsX3BsYXkoNTAsIFRydWUpLCBGYWxzZSksCiAgdGVzdChzcXVpcnJlbF9wbGF5KDEwMCwgRmFsc2UpLCBGYWxzZSksCiAgdGVzdChzcXVpcnJlbF9wbGF5KDEwMCwgVHJ1ZSksIFRydWUpLAogIHRlc3Qoc3F1aXJyZWxfcGxheSgxMDUsIFRydWUpLCBGYWxzZSksCiAgdGVzdChzcXVpcnJlbF9wbGF5KDU5LCBGYWxzZSksIEZhbHNlKSwKICB0ZXN0KHNxdWlycmVsX3BsYXkoNTksIFRydWUpLCBGYWxzZSksCQogIHRlc3Qoc3F1aXJyZWxfcGxheSg2MCwgRmFsc2UpLCBUcnVlKV0pOgogICAgcG9udG9zICs9IDUKCiAgaWYgYWxsKFsKICB0ZXN0KHBlZ29fY29ycmVuZG8oNjAsIEZhbHNlKSwgMCksCiAgdGVzdChwZWdvX2NvcnJlbmRvKDY1LCBGYWxzZSksIDEpLAogIHRlc3QocGVnb19jb3JyZW5kbyg2NSwgVHJ1ZSksIDApLAogIHRlc3QocGVnb19jb3JyZW5kbyg4MCwgRmFsc2UpLCAxKSwKICB0ZXN0KHBlZ29fY29ycmVuZG8oODUsIEZhbHNlKSwgMiksCiAgdGVzdChwZWdvX2NvcnJlbmRvKDg1LCBUcnVlKSwgMSksCiAgdGVzdChwZWdvX2NvcnJlbmRvKDcwLCBGYWxzZSksIDEpLAogIHRlc3QocGVnb19jb3JyZW5kbyg3NSwgRmFsc2UpLCAxKSwKICB0ZXN0KHBlZ29fY29ycmVuZG8oNzUsIFRydWUpLCAxKSwKICB0ZXN0KHBlZ29fY29ycmVuZG8oNDAsIEZhbHNlKSwgMCksCiAgdGVzdChwZWdvX2NvcnJlbmRvKDQwLCBUcnVlKSwgMCksCiAgdGVzdChwZWdvX2NvcnJlbmRvKDkwLCBGYWxzZSksIDIpXSk6CiAgICBwb250b3MgKz0gNQoKICBpZiBhbGwoWwogIHRlc3QoY291bnRfY29kZSgnYWFhY29kZWJiYicpLCAxKSwKICB0ZXN0KGNvdW50X2NvZGUoJ2NvZGV4eGNvZGUnKSwgMiksCiAgdGVzdChjb3VudF9jb2RlKCdjb3pleHhjb3BlJyksIDIpLAogIHRlc3QoY291bnRfY29kZSgnY296Znh4Y29wZScpLCAxKSwKICB0ZXN0KGNvdW50X2NvZGUoJ3h4Y296ZXl5Y29wJyksIDEpLAogIHRlc3QoY291bnRfY29kZSgnY296Y29wJyksIDApLAogIHRlc3QoY291bnRfY29kZSgnYWJjeHl6JyksIDApLAogIHRlc3QoY291bnRfY29kZSgnY29kZScpLCAxKSwKICB0ZXN0KGNvdW50X2NvZGUoJ29kZScpLCAwKSwKICB0ZXN0KGNvdW50X2NvZGUoJ2MnKSwgMCksCiAgdGVzdChjb3VudF9jb2RlKCcnKSwgMCksCiAgdGVzdChjb3VudF9jb2RlKCdBQWNvZGVCQmNvbGVDQ2Njb3JlREQnKSwgMyksCiAgdGVzdChjb3VudF9jb2RlKCdBQWNvZGVCQmNvbGVDQ2Njb3JmREQnKSwgMiksCiAgdGVzdChjb3VudF9jb2RlKCdjb0Fjb2RlQmNvbGVjY29yZUREJyksIDMpXSk6CiAgICBwb250b3MgKz0gNQoKICBpZiBhbGwoWwogIHRlc3QoZmlsYV90aWpvbG9zKDMsIDEsIDgpLCBUcnVlKSwKICB0ZXN0KGZpbGFfdGlqb2xvcygzLCAxLCA5KSwgRmFsc2UpLAogIHRlc3QoZmlsYV90aWpvbG9zKDMsIDIsIDEwKSwgVHJ1ZSksCiAgdGVzdChmaWxhX3Rpam9sb3MoMywgMiwgOCksIFRydWUpLAogIHRlc3QoZmlsYV90aWpvbG9zKDMsIDIsIDkpLCBGYWxzZSksCiAgdGVzdChmaWxhX3Rpam9sb3MoNiwgMSwgMTEpLCBUcnVlKSwKICB0ZXN0KGZpbGFfdGlqb2xvcyg2LCAwLCAxMSksIEZhbHNlKSwKICB0ZXN0KGZpbGFfdGlqb2xvcygzLCAxLCA3KSwgVHJ1ZSksCiAgdGVzdChmaWxhX3Rpam9sb3MoMSwgMSwgNyksIEZhbHNlKSwKICB0ZXN0KGZpbGFfdGlqb2xvcygyLCAxLCA3KSwgVHJ1ZSksCiAgdGVzdChmaWxhX3Rpam9sb3MoNywgMSwgMTEpLCBUcnVlKSwKICB0ZXN0KGZpbGFfdGlqb2xvcyg3LCAxLCA4KSwgVHJ1ZSksCiAgdGVzdChmaWxhX3Rpam9sb3MoNywgMSwgMTMpLCBGYWxzZSksCiAgdGVzdChmaWxhX3Rpam9sb3MoNDMsIDEsIDQ2KSwgVHJ1ZSksCiAgdGVzdChmaWxhX3Rpam9sb3MoNDAsIDEsIDQ2KSwgRmFsc2UpLAogIHRlc3QoZmlsYV90aWpvbG9zKDIyLCAyLCAzMyksIEZhbHNlKSwKICB0ZXN0KGZpbGFfdGlqb2xvcygwLCAyLCAxMCksIFRydWUpLAogIHRlc3QoZmlsYV90aWpvbG9zKDEwMDAwMDAsIDEwMDAsIDEwMDAxMDApLCBUcnVlKSwKICB0ZXN0KGZpbGFfdGlqb2xvcygyLCAxMDAwMDAwLCAxMDAwMDMpLCBGYWxzZSksCiAgdGVzdChmaWxhX3Rpam9sb3MoMTIsIDIsIDIxKSwgVHJ1ZSldKToKICAgIHBvbnRvcyArPSA1CgogIGlmIGFsbChbCiAgdGVzdChidXNjYSgnYW5hIGUgbWFyaWFuYSBnb3N0YW0gZGUgYmFuYW5hJywgJ2FuYScpLCA0KSwKICB0ZXN0KGJ1c2NhKCd1bWEgYXJhcmEgb3UgZHVhcyBhcmFyYXMnLCAnYXJhJyksIDQpLAogIHRlc3QoYnVzY2EoJ2FzYXNhc2FzYXNhc2FzYScsICdhc2EnKSwgNyldKToKICAgIHBvbnRvcyArPSA1CgogIGlmIGFsbChbCiAgdGVzdCh6ZigxMDEwMDEwMDAxMDAwMCksIDQpLAogIHRlc3QoemYoOTAwMDAwMDAwMDAwMDAwMDAwMTApLCAxKV0pOgogICAgcG9udG9zICs9IDUKCiAgaWYgYWxsKFsKICB0ZXN0KGNvbnRhMigyMCksIDIpLAogIHRlc3QoY29udGEyKDk5OSksIDMwMCksCiAgdGVzdChjb250YTIoNTU1KSwgMjE2KV0pOgogICAgcG9udG9zICs9IDUKCiAgaWYgYWxsKFsKICB0ZXN0KGluaXAyKDcpLCA0NiksCiAgdGVzdChpbmlwMigxMzMpLCAzMTYpLAogIHRlc3QoaW5pcDIoMTAyNCksIDEwKV0pOgogICAgcG9udG9zICs9IDUKCiAgcHJpbnQgKCdQb250b3M6ICVkLzEwMCcgJXBvbnRvcykKICAKaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoKICBtYWluKCkK'
eval(compile(b64decode(code), "<string>", 'exec'))
