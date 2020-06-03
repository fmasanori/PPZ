n = 908007000
print (len(str(n)) - len(str(int(str(n)[::-1]))))
print (len(str(n)) - len(str(n).rstrip('0')))
from itertools import takewhile
l = str(n).split('0')
print(len(list(takewhile(lambda x: not x, reversed(l)))))
import re
print(len(re.findall('0*$',str(n))[0]))
f = lambda m: (lambda g: g(m, g))(lambda n, f: 1 + f(n // 10, f) if n % 10 == 0 else 0)
print (f(n))
f = lambda x, y: y if x % 10 != 0 else f(x/10,y+1)
print (f(n, 0))
f = lambda n : 0 if n%10 else 1 + f(n//10)
print (f(n))
