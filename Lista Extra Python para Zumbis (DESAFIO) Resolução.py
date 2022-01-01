def vestibular():
  t = 93
  p = t // 5
  while (t - p * 5) % 7 != 0:
    p = p - 1
  g = (t - p * 5) // 7
  return f'{p} pequenos e {g} grandes' 

def dec2rom(n):
  uni = [''] + 'I II III IV V VI VII VIII IX'.split()
  dez = [''] + 'X XX XXX XL L LX LXX LXXX XC'.split()
  cen = [''] + 'C CC CCC CD D DC DCC DCCC CM'.split()
  mil = [''] + 'M MM MMM ~IV ~V ~VI ~VII ~VIII ~IX'.split()
  m = n // 1000
  n = n % 1000    
  c = n // 100
  n = n % 100
  d = n // 10
  n = n % 10
  u = n
  return mil[m] + cen[c] + dez[d] + uni[u]

def pi(n):
  k = 1
  impar = 1
  s = 0
  while k <= n:
    if k % 2 == 1:
      s = s + 4/impar
    else:
      s = s - 4/impar
    k = k + 1
    impar = impar + 2
  return s

