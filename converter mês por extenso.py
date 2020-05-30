def mês_por_extenso(data):
  mes = '''janeiro fevereiro março
      abril maio junho julho agosto
      setembro outubro novembro
      dezembro'''.split()

  d, m, a = data.split('/')

  return f'{d} de {mes[int(m)-1]} de {a}'
