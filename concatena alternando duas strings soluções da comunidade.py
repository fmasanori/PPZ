s1 = 'abacate'
s2 = 'palmeiras'
f1 = len(s1)
f2 = len(s2)
s = ''
for k in range(min(f1, f2)):
  s += s1[k]
  s += s2[k]
k += 1
s += s1[k:] if f1 > f2 else s2[k:]
print (s)
from itertools import chain, zip_longest
print (''.join(''.join(x) for x in
               zip_longest(s1, s2, fillvalue='')))
print (''.join(chain.from_iterable(
               zip_longest(s1, s2, fillvalue=''))))
print (''.join(chain(*zip_longest(s1, s2, fillvalue=''))))
#a primeira solução é original do Hélio Meira, do grupo do Facebook Python Programadores
#a segunda solução é do Tonny via Telegram https://t.me/pythonbr
#a terceira é do Paulo Freitas do Facebook Python Programadores
